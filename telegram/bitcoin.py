import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    r = requests.get(url)
    datas =r.json()
    print(datas,'\n')
    data = datas['ticker']['last']
    print(data)
    return str(data)

