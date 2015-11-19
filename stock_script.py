import urllib
import os
import collections
import sys

totals = {}
date_ranges = {}
data = collections.defaultdict(dict)
file_output = []

def printsymbols(sym_totals, output):
  for symbol, changes in reversed(sorted(sym_totals.iteritems(), key=lambda x: sym_totals[x[0]])):
    output += "%s    %s%%\n" % (symbol, changes)
  output += "\n"
  return output
  
def decode_files(window, symbol_list):
  global data, date_ranges
  for sym in symbol_list:
    with open("%s.csv" % sym) as sym_file:
      lines = sym_file.readlines()
    for start_row in range(1, len(lines)-window-1):
      new_window = window + start_row
      end_cols = lines[start_row].split(",")
      end_date = int(end_cols[0].replace("-", ""))
      end_price = float(end_cols[6])
      start_cols = lines[new_window].split(",")
      start_date = int(start_cols[0].replace("-", ""))
      start_price = float(start_cols[6])
      data[start_date][sym] = round((end_price-start_price)/start_price*100, 2)
      date_ranges[start_date] = end_date

def calculate_performance(window, symbol_list):
  global totals, file_output
  for symbol in symbol_list:
    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&g=w" % symbol.upper()
    if os.path.isfile("%s.csv" % symbol):
  	  os.remove("%s.csv" % symbol)
    urllib.urlretrieve(url, "%s.csv" % symbol.lower())
  decode_files(window, symbol_list)

  for date in sorted(date_ranges.keys()):
    if not all(s in data[date].keys() for s in symbol_list):
      continue
    total = sum(data[date].values())/len(symbol_list)
    totals[date] = total
    file_output.append("%d - %d    %.2f%%\n" % (date, date_ranges[date], total))
  if not totals:
    sys.exit("These stocks never sold at the same time!")

  highest_date = max(totals.keys(), key=(lambda k: totals[k]))
  highest = "%s - %s    %.2f%%" % (highest_date, date_ranges[highest_date], totals[highest_date])
  lowest_date = min(totals.keys(), key=(lambda k: totals[k]))
  lowest = "%s - %s    %.2f%%" % (lowest_date, date_ranges[lowest_date], totals[lowest_date])
  latest_date = sorted(date_ranges.keys())[-1]
  latest = "%s - %s    %.2f%%" % (latest_date, date_ranges[latest_date], totals[latest_date])

  output = ""
  output += "\n\nHIGHEST: %s\n" % highest
  output = printsymbols(data[highest_date], output)
  output += "LOWEST: %s\n" % lowest
  output = printsymbols(data[lowest_date], output)
  output += "LATEST: %s\n" % latest
  output = printsymbols(data[latest_date], output)
  file_output.append(output)

  for symbol in symbol_list:
    if os.path.isfile("%s.csv" % symbol):
  	  os.remove("%s.csv" % symbol)

  return output
  

def main():
  out = open("out.txt", 'w+')
  timeperiod = float(raw_input("Time Period in Months: "))
  window = int(round(timeperiod/12*365/7))
  symbols = raw_input("Symbols: ")
  symbol_list = [symbol.lower().strip() for symbol in symbols.split(",") if " " not in symbol.strip()]

  output = calculate_performance(window, symbol_list)
  print output
  
  out.write(''.join(file_output))
  out.flush()
  out.close()

if __name__=="__main__":
  main()