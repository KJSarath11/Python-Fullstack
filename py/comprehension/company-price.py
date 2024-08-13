#wapt building dictionary whose price valye is more than 200
prices={'ACME':45.23,'AAPL':612.78,'IBM':205.55,'FB':10.75}
price_200={}

for company,price in prices.items():#items selects both the keys-values
    if price>200:
        price_200[company]=price
print(price_200)

#comprehension
price_200={company:price for company,price in prices.items() if price>200}
print(price_200)