from confluent_kafka import Consumer, KafkaException, KafkaError


if __name__ == '__main__':
    topics = ['my-topic']
    group =['consumers1']

    config = {'bootstrap.servers': "localhost:9092", 'group.id': group}

    c = Consumer(config)

    def print_assignment(consumer, partitions):
        print('Assignment: ', partitions)

    # Subscribe to topics
    c.subscribe(topics, on_assign=print_assignment)

    # Read messages from Kafka, print to stdout
    try:
        while True:
            msg = c.poll()
            if msg is None:
                continue
            if msg.error():
                # Error or event
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                else:
                    # Error
                    raise KafkaException(msg.error())
            else:
                # Proper message
                print(msg.value())

    except KeyboardInterrupt:
        print('%% Aborted by user\n')

    finally:
        # Close down consumer to commit final offsets.
        c.close()