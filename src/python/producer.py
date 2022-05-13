"""Creates a producer"""

from random import choice
from confluent_kafka import Producer
from config import Configuration

if __name__ == '__main__':

    config = Configuration()

    producer = Producer(config.default)

    def delivery_callback(err, msg):
        """"Callback funciton"""
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}"
                .format(topic=msg.topic(),
                       key=msg.key().decode('utf-8'),
                       value=msg.value().decode('utf-8')))

    # Produce data by selecting random values from these lists.
    TOPIC = "purchases"
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']

    count = 0
    for _ in range(10):

        user_id = choice(user_ids)
        product = choice(products)
        producer.produce(TOPIC, product, user_id, callback=delivery_callback)
        count += 1

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()
