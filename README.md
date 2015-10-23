#stock-portfolio-predictions
A simple Python script that gives you the best, worst, and latest stock portfolio performace over a given frame of time.

This assumes you have equally invested your assets into each stock you give for your portfolio. Uses Yahoo! Finance as a historical stock data source.

You can use this tool so mix and match different portfolio options and quickly analyze its historical and latest performace. This also produces a text file (`out.txt`) with the performance for every time frame up to the present.

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

Snippet from `out.txt` from above command:
```
20150330 - 20140331    33.34%
20150406 - 20140407    38.12%
20150413 - 20140414    33.63%
20150420 - 20140421    35.98%
20150427 - 20140428    28.55%
20150504 - 20140505    29.50%
20150511 - 20140512    28.02%
20150518 - 20140519    25.72%
20150526 - 20140527    20.82%
20150601 - 20140602    18.90%
```

##Notes
Note that these numbers will not correspond exactly to what you would see on the Yahoo! Finance website since this uses adjusted stock prices to compensate for splits/mergers/etc.

This might crash if you use really shady stocks (eg if they haven't been on the market long) or some penny stocks since there's not enough data to crunch numbers.
