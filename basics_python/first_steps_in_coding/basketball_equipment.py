tax_basket = int(input())
basket_shoes = tax_basket - tax_basket * 0.4
basket_kit = basket_shoes - basket_shoes * 0.2
basket_ball = basket_kit / 4
basket_accesory = basket_ball / 5
price_to_pay = tax_basket + basket_shoes + basket_kit + basket_ball + basket_accesory
print(price_to_pay)
