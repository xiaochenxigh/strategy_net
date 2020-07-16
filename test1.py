from typing import List
from dataclasses import dataclass


@dataclass
class Ticker:
    exchange: str
    symbol: str
    buy: float
    sell: float


# Net，price,amount,订单编号，成交数量，下单时间，成交时间
@dataclass
class Order:
    order_id: str
    price: float
    amount: float
    deal: float
    create_time: str
    status: int


@dataclass
class PriceList:
    base_price: float
    every_diff: float
    depth: int
    price_decimal: int
    amount_dicimal: int
    buy_list = []

    def get_price_list(self):
        return [round(self.base_price - self.base_price * self.every_diff * i, self.price_decimal) for i in
                range(self.depth)]


@dataclass
class NetMin:
    price: float
    amount: float
    order_id: str


@dataclass
class Net:
    user: int
    account: int
    exchange: str
    symbol: str
    onoff: int
    base_price: float
    every_diff: float
    depth: int
    price_decimal: int
    amount_dicimal: int
    price_list: List[float] = None
    order_list: List[Order] = None

    def get_net(self):
        self.price_list = [round(self.base_price - self.base_price * self.every_diff * i, self.price_decimal) for i in
                           range(self.depth)]


def get_net_setting():
    return []


def get_ticker(exchange, symbol):
    return Ticker()


def net_main():
    setting = get_net_setting()
    for n in setting:
        user = n['user']
        account = n['account']
        exchange = n['exchange']
        symbol = n['symbol']
        onoff = n['onoff']
        base_price = n['base_price']
        every_diff = n['every_diff']
        amount = n['amount']
        profile = n['profile']
        if onoff != 1:
            continue
        ticker = get_ticker(exchange, symbol)
        if base_price == -1:  # 网格重置
            base_price = (ticker.buy + ticker.sell) / 2
            if base_price < 0:
                continue
