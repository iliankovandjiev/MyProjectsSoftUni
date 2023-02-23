def shop_from_grocery_list(budget, products, *grocery_list):
    for product, price in grocery_list:
        if product in products:
            if budget >= price:
                budget -= price
                products.remove(product)
            else:
                break

    if not products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(products)}."


