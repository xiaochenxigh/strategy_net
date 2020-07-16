"""
1. 网格标识（用户，帐户，品种）
2. 网格交易表（基础价格，每格价差，数量，是否有订单)
3. 订单维护（盈利比率）
"""
from typing import List
from dataclasses import dataclass


@dataclass
class Ticker:
    buy: float
    sell: float


class Order:
    order_id: str


@dataclass
class Net:
    user: int
    account: int
    exchange: str
    symbol: str
    price_decimal: int
    amount_dicimal: int
    onoff: int
    base_price: float
    every_diff: float
    depth: int
    amount: float
    profile: float
    price_list: List[float] = None
    order_list: List[]

    def set_net(self, price):
        self.price_list = [round(price - price * self.every_diff * i, self.price_decimal) for i in
                           range(self.depth)] + [round(price + price * self.every_diff * i, self.price_decimal) for i in
                                                 range(self.depth)]

    def get_net(self):
        pass

    def get_price(self):
        pass

    def open_orders(self):
        pass


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
        net = Net(user, account, symbol, onoff, base_price, every_diff, amount, profile)
        if net.onoff != 1:
            continue
        ticker = get_ticker(net.exchange, net.symbol)
        if net.price_list is None:
            net.set_net((ticker.buy + ticker.sell) / 2)
        # 将网格写入数据库


def create_order(net: Net, ticker: Ticker):
    # 遍历网格
    buy_list = []
    for i in range(net.depth):
        # 如果卖单小于我们要买入的网格，则挂限价单买入
        if ticker.sell < net.price_list[i]:
            price = net.price_list[i]
            amount = round((net.amount / price), net.amount_dicimal)
            buy_list.append([price, amount])
    # 执行挂单，将挂单的信息写入数据库，et： Net，price,amount,订单编号，成交数量，下单时间，成交时间


def check_orders(order_id):
    # 根据order_id查询到网格编号
    # 已成交判断是否可卖出
    # 卖出查成交，得出利润
    pass



