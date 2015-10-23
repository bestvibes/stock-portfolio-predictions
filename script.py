import urllib
import os
import collections

def printsymbols(sym_totals):
  result = {}
  for symbol, changes in reversed(sorted(sym_totals.iteritems(), key=lambda x: sym_totals[x[0]])):
    print symbol + "    " + str(changes)
  print "\n"
  
def decode_files(sym_list, window):
  data = collections.defaultdict(dict)
  dates = {}
  for sym in sym_list:
    with open(sym + ".csv") as sym_file:
      lines = sym_file.readlines()
    for start_row in range(1, len(lines)-window-1):
      new_window = window + start_row
      start_cols = lines[start_row].split(",")
      start_date = int(start_cols[0].replace("-", ""))
      start_price = float(start_cols[6])
      end_cols = lines[new_window].split(",")
      end_date = int(end_cols[0].replace("-", ""))
      end_price = float(end_cols[6])
      data[start_date][sym] = round((start_price-end_price)/end_price*100, 2)
      dates[start_date] = end_date
  return data, dates

def main():
  out = open("out.txt", 'w+')
  totals = {}
  timeperiod = float(raw_input("Time Period in Months: "))
  window = int(round(timeperiod/12*365/7))
  symbols = raw_input("Symbols: ")
  symbol_list = [symbol.lower().strip() for symbol in symbols.split(",")]

  for symbol in symbol_list:
	  url = "http://ichart.finance.yahoo.com/table.csv?s=" + symbol.upper() + "&g=w"
	  if os.path.isfile(symbol+".csv"):
		  os.remove(symbol+".csv")
	  urllib.urlretrieve(url, symbol.lower()+".csv")
  data, dates = decode_files(symbol_list, window)

  for date in sorted(dates.keys()):
    if not all(s in data[date].keys() for s in symbol_list):
      continue
    total = sum(data[date].values())/len(symbol_list)
    totals[date] = total
    out.write("%d - %d    %.2f%%" % (date, dates[date], total) + "\n")
  if not totals:
    print "These stocks never sold at the same time!"
    return

  highest_date = max(totals.keys(), key=(lambda k: totals[k]))
  highest = "%s - %s    %.2f%%" % (highest_date, dates[highest_date], totals[highest_date])
  lowest_date = min(totals.keys(), key=(lambda k: totals[k]))
  lowest = "%s - %s    %.2f%%" % (lowest_date, dates[lowest_date], totals[lowest_date])
  latest_date = sorted(dates.keys())[-1]
  latest = "%s - %s    %.2f%%" % (latest_date, dates[latest_date], totals[latest_date])
  out.write("HIGHEST: " + highest + "\n")
  out.write("LOWEST: " + lowest + "\n")
  out.write("LATEST: " + latest + "\n")
  print "\n\nHIGHEST: " + highest
  printsymbols(data[highest_date])
  print "LOWEST: " + lowest
  printsymbols(data[lowest_date])
  print "LATEST: " + latest
  printsymbols(data[latest_date])

if __name__=="__main__":
  main()