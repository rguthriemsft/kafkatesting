set -euo pipefail

# use a virtual environment
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# mkdir .download
# pushd .download
# wget https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz
# tar -xvf kafka_2.13-3.1.0.tgz
# mv -t ./kafka_2.13-3.1.0.tgz /usr/local/bin/kafka_2.13-3.1.0