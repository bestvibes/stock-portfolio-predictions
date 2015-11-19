#stock-portfolio-predictions
A simple Python script that gives you the **best, worst, and latest stock portfolio performace** over a given frame of time.

**This assumes you have equally invested your assets** into each stock you give for your portfolio. More flexibility with this is in the works. Uses Yahoo! Finance as a historical stock data source.

You can use this tool to **mix and match different portfolio options and quickly analyze its historical and latest performance**. This also produces a text file (`out.txt`) with the performance for every time frame up to the present.

##Running
```
Vaibhavs-MacBook-Pro:stocks vaibhavaggarwal$ python script.py 
Time Period in Months: 12  
Symbols: aapl,googl


HIGHEST: 20040907 - 20050906    185.03%
aapl    186.09%
googl    183.96%

LOWEST: 20071224 - 20081222    -57.16%
aapl    -57.06%
googl    -57.25%

LATEST: 20141117 - 20151116    20.82%
googl    39.22%
aapl    2.42%
```

Snippet from `out.txt` from above command:
```
20041004 - 20051003    144.96%
20041011 - 20051010    121.43%
20041018 - 20051017    115.96%
20041025 - 20051024    97.89%
20041101 - 20051031    127.03%
20041108 - 20051107    118.14%
20041115 - 20051114    135.14%
20041122 - 20051121    126.89%
20041129 - 20051128    131.64%
20041206 - 20051205    133.28%
```

##Notes
Note that these numbers will not correspond exactly to what you would see on the Yahoo! Finance website since this uses adjusted stock prices to compensate for splits/mergers/etc.

This might crash if you use really shady stocks (eg if they haven't been on the market long) or some penny stocks since there's not enough data to crunch numbers.
