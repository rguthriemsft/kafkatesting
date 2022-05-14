# Samples for using kafka cli (/usr/local/bin/confluent/bin)

See [kafka documentation](https://kafka.apache.org/documentation/#basic_ops) for many exmples of how to use the cli.

## kafka-console-producer and kafka-console-consumer

```bash

# Start producer
kafka-console-producer --topic purchases --bootstrap-server localhost:29092

# Start consumer
kafka-console-consumer --topic purchases --from-beginning --bootstrap-server localhost:29092

```