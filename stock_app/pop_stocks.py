from yahoo_finance import Share
from itertools import product
from string import ascii_uppercase
from django.utils import timezone

from .models import Stock

# This function is used to populate the database with all known stock tickers. It creates a list of all possible tickers
# and then adds the information to the database for the tickers that exist.


def populate_stocks():
    ticker_list = []

    for i in range(1,6):
        ticker_list.extend(list(map(''.join, product(ascii_uppercase, repeat=i))))

    for tick in ticker_list:
        print("Checking " + tick + ".")
        if Share(tick).get_name():
            try:
                if Stock.objects.get(ticker=tick):
                    print(tick + " already exists. Skipping database entry.")
                    continue
            except:
                stock_info = Share(tick)
                stock = Stock(
                    name=stock_info.get_name(),
                    ticker=tick,
                    price=stock_info.get_price(),
                    price_target=stock_info.get_one_yr_target_price(),
                    is_bullish=None,
                    last_updated=timezone.now()
                )
                stock.save()

                print(tick + " " + Share(tick).get_name())


