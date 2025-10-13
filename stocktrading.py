def optimizeTradingGains(prices):
    #This problem requires us to keep track of the difference between two numbers as we iterate down through a list. Ok, so now, I know that this should at least be a sliding window problem that requires a time complexity of at least O(n). I don't anticipate any space complexity beyond O(1). Anyway, we're given a list of integers (hopefully we can assume they're all truly integers!), and we are expected to return an integer denoting the maximum profit we could potentially make. This problem would backfire if we only have one value inside the list. It is illogical to make a profit if there is no other potential selling day. Nevertheless, you can do the following to solve: (I forgot to mention that sliding window problems are often synonymous with using two pointers)
    #We can initialize a profit to 0, changing this overtime as we iterate through our list
    #We'll also initialize our first pointer without an index, thanks to Python's iteration semantics.
    #Once we iterate through the array, we'll go over each potential selling price in the array. If it is less than buy (our first value), then no profit can be made, so we set buy to sell. Becuase sell will always advance, that's our 'second pointer'.
    #Otherwise, we'd set profit to the maximum value comparing our previous profit and the difference between sell and buy. This is important because we can't be hasty, reckless buyers, settling for the first profit we see. We must be patient and wait to see if there are more profits to be made and also compare our current profit to our most recent profit to see which one is greater.
    #After all of this, we return profit
    profit = 0
    buy = prices[0]
    for sell in prices:
        if buy > sell:
            buy = sell
        else:
            profit = max(profit, sell - buy)
    return profit
    
