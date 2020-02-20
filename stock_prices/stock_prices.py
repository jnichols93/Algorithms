#!/usr/bin/python

import argparse

# find_max_profit([1050, 270, 1540, 3800, 2])
# returns 3530

def find_max_profit(prices):
 # Return the max profit that can be made from a single buy and sell 
 # Set the current  min price equal to first price in the list 
    current_min = prices[0] 
# set the max profit equal to first price subtracted from max price in the list
    max_profit = prices[1] - prices[0] 

    for i in range(1, len(prices)):
  # if the index of price is less than the current min prices,
  # then the current min price is equal to the index of prices
      if prices[i] < current_min:
        current_min = prices[i]
        # print(current_min,'this is min')
  # else if the diff betwen the index of prices and the current min 
  # price is greater than the current max profit, 
  #then the max profit is equal to th diff between the min and max prices
      elif prices[i] - current_min > max_profit:
        max_profit = prices[i] - current_min
        # print(max_profit,'this is max')

    return max_profit
print(find_max_profit([1050, 270, 1540, 3800, 2]))



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()


  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))