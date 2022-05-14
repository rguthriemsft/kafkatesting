# Notes

## Videos - getting started

- confluent cloud creates topcis with 6 partitions by default.
- Topics - topic is a log.  
  - Append only
	- Seek by offset, not indexed
	- Events are immutable, can't unhappen. Easier to make copies because of this.
	- Sustain high throughput in/out of topics
	- Logs are durable, nothing inherently temporary in a log. Logs are files and durable.
	- Retention is configurable
- Partitioning
	- Topics can span many machines
	- Takes single topic log and breaks into multiple logs, each of which can live on a seperate node in the cluster.
	- Key is how Kafka decides which partition to write message to.  If no key, messages are distributed between partitions using round-robin (hash function).
	- Kafka guarantees that messages having same key always land in same partition and in order.
	- Active key can create a hot partition. 
	




## Tools

- [CLI and how-to](https://hevodata.com/learn/kafka-cli)
- [aiokafka](https://github.com/aio-libs/aiokafka)
- [Exactly Once Consumer](https://www.thebookofjoel.com/python-kafka-consumers)

## [librdkafka](https://github.com/edenhill/librdkafka)

- [Confluent Kafka Client configuration docs](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#kafka-client-configuration) 

- [Introduction](https://github.com/edenhill/librdkafka/blob/master/INTRODUCTION.md)
- [Full exactly once semantics (EOS) transactional consumer-producer exammpl](https://github.com/edenhill/librdkafka/tree/master/examples)
- [Configuration parameters](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md)
- []()
