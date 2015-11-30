# natural_gas_prices
A scraper for the daily Henry Hub Natural Gas Spot price from http://www.eia.gov/dnav/ng/hist/rngwhhdD.htm

1. First run get_prices_table.py to get the whole table and save it to a text file.

2. Second run parse_table.py to parse the table, fill in missing values, fill in for missing week in the data, save it to daily_prices.csv and resampled to monthly_prices.csv where the date is the first business day of the month.

3. Script needs to be edited for updates, so that when it's run it only adds new dates to the CSV's.
