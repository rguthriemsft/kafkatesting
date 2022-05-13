#!/bin/bash
set -euo pipefail
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

CONFIG="${SCRIPT_DIR}/localhost.config"
BOOTSTRAP_SERVER=$(grep -oP "bootstrap.servers=\K.*" "${CONFIG}")
TOPIC=perf-test-topic
PARTITIONS=4

THROUGHPUT=200
RECORD_SIZE=1000
NUM_RECORDS=3000
PRODUCER_PROPS="linger.ms=0 batch.size=16384"

kafka-topics \
    --bootstrap-server "${BOOTSTRAP_SERVER}" \
    --delete \
    --if-exists \
    --topic "${TOPIC}"

kafka-topics \
    --bootstrap-server "${BOOTSTRAP_SERVER}" \
    --create \
    --topic "${TOPIC}" \
    --partitions ${PARTITIONS}

kafka-producer-perf-test \
    --producer.config "${CONFIG}" \
    --throughput ${THROUGHPUT} \
    --record-size ${RECORD_SIZE} \
    --num-records ${NUM_RECORDS} \
    --topic "${TOPIC}" \
    --producer-props ${PRODUCER_PROPS} \
    --print-metrics | grep \
"3000 records sent\|\
producer-metrics:outgoing-byte-rate\|\
producer-metrics:bufferpool-wait-ratio\|\
producer-metrics:record-queue-time-avg\|\
producer-metrics:request-latency-avg\|\
producer-metrics:batch-size-avg"

