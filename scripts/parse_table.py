import sys
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

with open("html_table.txt", "r") as f:
    table = f.read()
dates = []

table = bs(table)
table_rows = table.findAll("tr")


for element in table_rows[1:]:
    for date_string in element.findAll("td", class_="B6"):
        date_string = date_string.text.encode("utf-8")
        date_string = date_string.split("to")
        date_string = date_string[0]
        date_string = date_string.replace(" ", "")
        year = int(date_string[4:8])
        date_string = date_string[8:]
        date_string = date_string.split("-")
        if date_string[0] == "Jan":
            date_string[0] = 1
        elif date_string[0] == "Feb":
            date_string[0] = 2
        elif date_string[0] == "Mar":
            date_string[0] = 3
        elif date_string[0] == "Apr":
            date_string[0] = 4
        elif date_string[0] == "May":
            date_string[0] = 5
        elif date_string[0] == "Jun":
            date_string[0] = 6
        elif date_string[0] == "Jul":
            date_string[0] = 7
        elif date_string[0] == "Aug":
            date_string[0] = 8
        elif date_string[0] == "Sep":
            date_string[0] = 9
        elif date_string[0] == "Oct":
            date_string[0] = 10
        elif date_string[0] == "Nov":
            date_string[0] = 11
        elif date_string[0] == "Dec":
            date_string[0] = 12
        date_string[1] = int(date_string[1])
        year = int(year)
        current_date = date(year=year, month=date_string[0], day=date_string[1])
        dates.append(current_date)


first_date = dates[0]
last_date = dates[-1] + timedelta(days=4)

values = []

for row in table_rows[1:]:
    for value in row.findAll("td", class_="B3"):
        
        value = value.text

        try:
            float(str(value))
        except ValueError:
            value = "N/A"
        values.append(value)

index = pd.date_range(start=first_date, end=last_date, freq="B")

df = pd.DataFrame()

df["date"] = index
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
df = df.set_index(df["date"])
mondays = df.loc[df.index.dayofweek == 0]["date"]
mondays = pd.to_datetime(mondays, format="%Y%m%d")


missing_date = set(mondays.index.date.tolist()).difference(set(dates))
missing_date = missing_date.pop()


counter = 0
for date_ in mondays:
    counter +=1
    if date_.strftime("%Y-%m-%d") == str(missing_date):
        break
counter = counter * 5 - 1
for i in range(5):
    values.insert(counter, "N/A")

df["price"] = values
df.to_csv("data/daily_prices.csv", index=False)
df = df.resample("BMS", how="first")
df.to_csv("data/monthly_prices.csv", index=False)
