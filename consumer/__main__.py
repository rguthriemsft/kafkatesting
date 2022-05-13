import signal
import sys
from confluent_kafka import Consumer

topic = "mytopic"
c = Consumer(
    {
        "bootstrap.servers": "localhost:29092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)


def signal_handler(sig, frame):
    print("exiting")
    c.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

c.subscribe([topic])
print(f"subscribed to {topic}")

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    print(f"Received message [{msg.partition()}]: {msg.value().decode('utf-8')}")
