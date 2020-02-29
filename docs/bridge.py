from binance.client import Client
from binance.websockets import BinanceSocketManager
api_key = 'NCluwdkB0aM4qO5XsSWsVHE3WZ22QJXrnybse9EfsW3hdAdi3VqZRMaC2CCTmV1D';
api_secret = 'iPkwtKkfq7iCwCnJFwYyLau5xwCF92P3cnQBNbPZ2z13CHfl6alJFO3mDeAr7Zun';
client = Client(api_key, api_secret)

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
# then start the socket manager
bm.start()