#stock-portfolio-predictions
A simple Python script that gives you the best, worst, and latest stock portfolio performace over a given frame of time.

Uses Yahoo! Finance as a historical stock data source.

##Running
```
Vaibhavs-MacBook-Pro:stock-portfolio-performance vaibhavaggarwal$ python script.py 
Time Period in Months: 12
Symbols: aapl,goog


HIGHEST: 20150406 - 20140407    38.12%
aapl    74.47
goog    1.77


LOWEST: 20150817 - 20140818    5.65%
aapl    6.17
goog    5.14


LATEST: 20151019 - 20141020    16.20%
goog    20.75
aapl    11.65
```

##Notes
Note that these numbers will not correspond exactly to what you would see on the Yahoo! Finance website since this uses adjusted stock prices to compensate for splits/mergers/etc.

This might crash if you use really shady stocks (eg if they haven't been on the market long) or some penny stocks since there's not enough data to crunch numbers.
