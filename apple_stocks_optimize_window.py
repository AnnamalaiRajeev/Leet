stock_prices = [10, 9,8,7,6,4]


def get_max_profit(stock_prices):
    difference = 0
    for i, buying_price in enumerate(stock_prices):
        for j in range(len(stock_prices)-1, i, -1):
            selling_price = stock_prices[j]
            if selling_price > buying_price:
                print(selling_price, buying_price)
                difference = max(selling_price-buying_price, difference)

    return difference


def get_max_profit_1(stock_prices):
    window_start = 0
    window_end = len(stock_prices)-1
    difference = 0
    while window_start < window_end:
        selling_price = stock_prices[window_end]
        buying_price = stock_prices[window_start]
        if selling_price > buying_price:
            difference = max(selling_price - buying_price, difference)
        if stock_prices[window_start+1] < stock_prices[window_start]:
            window_start += 1
        elif stock_prices[window_end-1] > stock_prices[window_end]:
            window_end -= 1
        else:
            stock_prices[window_start] += 1
    return difference



print(get_max_profit_1(stock_prices))
