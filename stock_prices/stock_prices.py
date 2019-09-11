#!/usr/bin/python

import argparse

# prices = [ 310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# prices = [1050, 270, 1540, 3800, 2]
prices = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
    # buy = 0
    # sell = 0
    max_difference = -10

    
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_difference:
                max_difference = prices[j] - prices[i]

    return max_difference

print(find_max_profit(prices))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
