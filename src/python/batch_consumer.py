from confluent_kafka import Consumer
import sys


if __name__ == '__main__':
    broker = "localhost:9092"
    group = "python-group"
    topics = ["cli-topic"]

    conf = {'bootstrap.servers': broker, 'group.id': group, 'session.timeout.ms': 6000,
            'auto.offset.reset': 'earliest'}
    c = Consumer(conf)

    def print_assignment(_, partitions):
        print('Assignment:', partitions)

    c.subscribe(topics, on_assign=print_assignment)

    while True:
        msg = c.poll(1)
        if msg is None:
            continue
        else:
            # Proper message
            sys.stderr.write(f'{msg.topic()} [{msg.partition()}] at offset {msg.offset()} with key {msg.key()}:\n')
            print(msg.value())
