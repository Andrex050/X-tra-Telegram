from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from userbot.events import register


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters1 = {
    "start" : "5",
    "limit" : "2",
    "convert" : "USD"

}
parameters2 = {
    "start" : "1",
    "limit" : "1",
    "convert" : "USD"
}
parameters3 = {
    "start" : "5",
    "limit" : "2",
    "convert" : "EUR"
}
parameters4 = {
    "start" : "1",
    "limit" : "1",
    "convert" : "EUR"
}
headers = {
  "Accepts" : "application/json",
  "X-CMC_PRO_API_KEY" : "d9e0d355-d56e-49c8-808b-b0b08517d4c5",
}

session = Session()
session.headers.update(headers)

@register(pattern=".btcprice")
async def who(event):
    if event.fwd_from:
        return
    try:
        ###########################################################
        """PRICE BCH US"""
        response = session.get(url, params=parameters1)
        data = json.loads(response.text)
        priceBCH_US = data["data"][0]["quote"]["USD"]["price"]
        """PRICE BTC US"""
        response = session.get(url, params=parameters2)
        data1 = json.loads(response.text)
        priceBTC_US = data1["data"][0]["quote"]["USD"]["price"]
        """PRICE BCH EUR"""
        response = session.get(url, params=parameters3)
        data1 = json.loads(response.text)
        priceBCH_EUR = data1["data"][0]["quote"]["EUR"]["price"]
        """PRICE BTC EUR"""
        response = session.get(url, params=parameters4)
        data1 = json.loads(response.text)
        priceBTC_EUR = data1["data"][0]["quote"]["EUR"]["price"]
        ########################################################
        await event.edit("𝟏 ฿𝐢𝐭𝐜𝐨𝐢𝐧 𝐯𝐚𝐥𝐞: \n\n" + "`" + str(("{0:.2f}".format(round(priceBTC_US,2)))) + "`" + "\n🅤🅢🅓 - $\n" + "`" + str(("{0:.2f}".format(round(priceBTC_EUR,2)))) + "`" + "\n🅔🅤🅡🅞 - €\n\n\n" + "𝟏 ฿𝐜𝐡 "                                                                                    
                                                                                                            "𝐯𝐚𝐥𝐞: \n\n" + "`" + str(("{0:.2f}".format(round(priceBCH_US,2)))) + "`" + "\n🅤🅢🅓 - $\n" + "`" + str(("{0:.2f}".format(round(priceBCH_EUR,2)))) +"`" + "\n🅔🅤🅡🅞 - €")
    except (ConnectionError, Timeout, TooManyRedirects)as e:
        print(e)