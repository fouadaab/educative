from cmath import inf
from typing import List

stock_prices = [310, 315, 275, 295, 260, 290, 230, 255, 250]
def buy_and_sell_stock_once(prices: List[int]) -> int:
    _min = inf
    _profit = 0
    for i in prices:
        if i < _min:
            _min = i
        else:
            _profit = max(_profit, i - _min)
        
    return _profit

print(buy_and_sell_stock_once(stock_prices))