def item_order(order):

    saladCount = order.count('salad')
    waterCount = order.count('water')
    hamburgerCount = order.count('hamburger')

    order = str("salad:")+str(saladCount)+str(" hamburger:")+str(hamburgerCount)+str(" water:")+str(waterCount)

    return order

print item_order("salad water hamburger salad hamburger")