import asyncio
import json

from src.consumers.base_consumer import Consumer

if __name__ == '__main__':
    amber_msg = \
        {
            'jsonrpc': '2.0',
            'method': 'subscribe',
            'params': ['market:futures:ohlcv', {'instrument': 'XRPUSDT', 'exchange': 'binance'}],
            'id': 1,
        }

    amber_header = {'x-api-key': 'xxxxx'}

    amber_endpoint = 'wss://ws.web3api.io/futures'

    deribit_msg_option = \
        {"jsonrpc": "2.0",
         "method": "public/subscribe",
         "id": 42,
         "params": {
             "channels": ["trades.option.any.100ms"]}
         }

    deribit_msg_spot = \
        {"jsonrpc": "2.0",
         "method": "public/subscribe",
         "id": 42,
         "params": {
             "channels": ["trades.spot.any.100ms"]}
         }

    deribit_msg_future = \
        {"jsonrpc": "2.0",
         "method": "public/subscribe",
         "id": 42,
         "params": {
             "channels": ["trades.future.any.100ms"]}
         }

    deribit_endpoint = 'wss://www.deribit.com/ws/api/v2'

    deribit_spot = Consumer(deribit_endpoint, json.dumps(deribit_msg_spot), None, 'test_topic', 'spot')
    deribit_future = Consumer(deribit_endpoint, json.dumps(deribit_msg_future), None, 'test_topic', 'future')

    multiple_coroutines = [deribit_spot.call_api(), deribit_future.call_api()]
    asyncio.get_event_loop().run_until_complete(asyncio.gather(*multiple_coroutines))