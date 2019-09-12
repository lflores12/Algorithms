#!/usr/bin/python

#find_max_profit([1050, 270, 1540, 3800, 2])

import argparse


def find_max_profit(prices):
    # find the maximum prfit possible of the stock prices.
    # you have to buy first and then sell on one of the folloing numbers. you cant go back in "time" or previous numbers
    # for every number in stock prices given
    max_profit_so_far = prices[1] - prices[0]
    for p in range(1, len(prices)):
        current_min_price_so_far = prices[p]

        for s in range(p+1, len(prices)):
            profit = prices[s] - current_min_price_so_far
            if profit > max_profit_so_far:
                max_profit_so_far = profit

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
