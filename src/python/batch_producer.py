from confluent_kafka import Producer
import sys

if __name__ == '__main__':
    broker = "localhost:9092"
    topic = "cli-topic"

    conf = {'bootstrap.servers': broker}

    p = Producer(**conf)

    def delivery_callback(err, msg):
        if err:
            sys.stderr.write(f'Message failed delivery: {err}\n')
        else:
            sys.stderr.write(f'Message delivered to {msg.topic()} {msg.partition()} @ {msg.offset()}\n')

    batch = []
    for n in range (1, 16):
        batch.append(f'message {n}')
        if n%5 == 0:
            for lines in batch:
                p.produce(topic, lines, callback=delivery_callback)
            batch = []
            p.poll(100)

    p.flush()
