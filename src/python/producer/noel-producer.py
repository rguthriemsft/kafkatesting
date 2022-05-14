from confluent_kafka import Producer, KafkaException, KafkaError
from confluent_kafka.admin import AdminClient, NewTopic


a = AdminClient({"bootstrap.servers": "127.0.0.1:29092"})
fs = a.create_topics(
    [
        NewTopic(
            "mytopic",
            num_partitions=4,
            replication_factor=2,
            config={"min.insync.replicas": 2},
        )
    ]
)

# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print(f"Topic {topic} created")
    except KafkaException as e:
        # print(f"Failed to create topic {topic}: {e}")
        error = e.args[0]
        if error.code() != KafkaError.TOPIC_ALREADY_EXISTS:
            raise e


p = Producer(
    {
        "bootstrap.servers": "127.0.0.1:29092",
        "enable.idempotence": True,
        "acks": "all",
        # "batch.num.messages": 1,
    }
)


def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush()."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


some_data_source = [str(i) for i in range(1000)]
for data in some_data_source:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce("mytopic", data.encode("utf-8"), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()