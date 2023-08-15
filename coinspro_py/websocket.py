import websockets
import asyncio
import json

class WebSocket:
    def __init__(self):
        self.uri_socket = "wss://wsapi.pro.coins.ph/openapi/quote/ws/v3/"
        self.callbacks = []

    async def subscribe(self, stream):
        async with websockets.connect(self.uri_socket) as ws:
            subscribe_request = {
                "method": "SUBSCRIBE",
                "params": [stream["stream_name"]],
                "id": stream["id"]
            }
            await ws.send(json.dumps(subscribe_request))

            while True:
                response = await ws.recv()

                data = json.loads(response)
                for callback in self.callbacks:
                    callback(data)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    async def handle_multi_streams(self, streams, callback):
        self.add_callback(callback)
        
        tasks = [self.subscribe(stream) for stream in streams]
        await asyncio.gather(*tasks)
