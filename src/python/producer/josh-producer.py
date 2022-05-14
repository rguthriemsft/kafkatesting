from confluent_kafka import Producer

config = {'bootstrap.servers': 'localhost:9092', 'message.max.bytes': '1000', 'enable.idempotence': 'true', 'acks': 'all'}


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer = Producer(config)
topic = "my-topic"

def send():
    for i in range(0, 100):
        try:
            producer.produce(topic, str(i), callback=acked)
        except BufferError as e:
            print('%% Local producer queue is full (%d messages awaiting delivery): try again\n' % len(producer))

        producer.poll(0)

send()

# Wait until all messages have been delivered
print('%% Waiting for %d deliveries\n' % len(producer))
producer.flush()