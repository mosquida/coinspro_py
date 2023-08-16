import websockets
import asyncio
import json

class WebSocket:
    def __init__(self):
        self.uri_socket = "wss://wsapi.pro.coins.ph/openapi/quote/ws/v3/"

    async def subscribe(self, stream, callback):
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
                callback(data)

   
    async def subscribe_streams(self, streams, callback):
        
        tasks = [self.subscribe(stream, callback) for stream in streams]
        await asyncio.gather(*tasks)