pens = int(input())
markers = int(input())
cleaners = int(input())
dis = int(input())
discount_per = dis / 100
money_total = (pens * 5.8 + markers * 7.2 + cleaners * 1.2)
money_needed = money_total - (money_total * discount_per)
print(money_needed)
