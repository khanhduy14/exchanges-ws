import configparser
from typing import List

import websockets
from kafka import KafkaProducer


class BootstrapConfig():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('configuration.ini')
        print(config)
        kafka_config = config['kafka.config']
        self.bootstrap = kafka_config['bootstrap_servers']

    @property
    def bootstrap(self) -> List[str]:
        return self._bootstrap

    @bootstrap.setter
    def bootstrap(self, value):
        self._bootstrap = value


class Consumer():
    def __init__(self, endpoint: str, msg, headers=None, topic=None, kind=None):
        self.kafka_config = BootstrapConfig()
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_config.bootstrap)
        self.endpoint = endpoint
        self.msg = msg
        self.headers = headers
        self.topic = topic
        self.cnt = 0
        self.kind = kind

    async def call_api(self):
        if self.headers:
            async with websockets.connect(self.endpoint, extra_headers=self.headers) as websocket:
                await websocket.send(self.msg)
                while websocket.open:
                    response = await websocket.recv()
                    data = bytearray(response.encode())
                    self.producer.send(self.topic, data)
                    self.producer.flush()
                    self.cnt += 1
                    print('processed {} data number {} with size {}'.format(self.kind, self.cnt,
                                                                            data.__sizeof__()))
        else:
            async with websockets.connect(self.endpoint) as websocket:
                await websocket.send(self.msg)
                while websocket.open:
                    response = await websocket.recv()
                    data = bytearray(response.encode())
                    self.producer.send(self.topic, data)
                    self.producer.flush()
                    self.cnt += 1
                    print('processed {} data number {} with size {}'.format(self.kind, self.cnt,
                                                                            data.__sizeof__()))
