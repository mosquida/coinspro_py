import asyncio
from coinspro_py import CoinsPro

coinspro = CoinsPro()

STREAMS = [
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
    {
        "id": "candlestick",
        "symbol": "btcusdt",
        "stream_name": "btcusdt@kline_1m"
    },
]

# DO SOMETHING WITH DATA
def handle_data(data):
    print("Received data: \n", data)

async def main():
    await coinspro.websocket.handle_multi_streams(streams=STREAMS, callback=handle_data)

asyncio.run(main())
