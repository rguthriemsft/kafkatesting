# kafka

## Ramp up Plan

1. [Getting started with Kafka](https://developer.confluent.io/learn-kafka/architecture/get-started/)
1. Use docker compose to create Kafka cluster
   1. `./start-kafka`
1. Connect to kafka
   1. VS Code (From recommended extensions)
   1. UI for Apache Kafka (Already part of local docker-compose.yaml)
1. Create Topics - learn about different options while creating topics
   1. Use extension
   1. Use UI
   1. Use CLI (Hint: exec into broker container)
1. Test cluster using command line
   1. Produce and consume from CLI
   1. Produce from CLI - see the messages in the UI and the VS Code Extension
1. Create simple python producer
1. Create simple python consumer
1. Add method to send batch of messages in producer
1. Add method to receive batch of messages in consumer
1. Create at-least once consumer
1. Create at most once consumer
1. Create exactly once consumer using transactions
1. Create consumer that handles de-duplication
