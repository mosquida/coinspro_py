import asyncio
from coinspro_py import CoinsPro

coinspro = CoinsPro()

MULTI_STREAMS = [
    {
        "id": "aggTrade",
        "symbol": "btcusdt",
        "stream_name": "btcusdt@aggTrade"
    },
    {
        "id": "trade",
        "symbol": "btcusdt",
        "stream_name": "btcusdt@trade"
    },

]

SINGLE_STREAMS = [
        {
        "id": "candlestick",
        "symbol": "btcusdt",
        "stream_name": "btcusdt@kline_1m"
    },
]

# DO SOMETHING WITH DATA
def handle_data(data):
    print("Received from multi stream: \n", data, "\n")

def handle_data_2(data):
    print("Received from single data stream: \n", data, "\n")

# SAMPLE SINGLE/ MULTI STREAM SUBSCRIPTION
async def main():
    await asyncio.gather(
        coinspro.websocket.subscribe_streams(streams=MULTI_STREAMS, callback=handle_data),
        coinspro.websocket.subscribe_streams(streams=SINGLE_STREAMS, callback=handle_data_2)
    )
    
asyncio.run(main())
