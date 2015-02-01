print("Miles", "Kilometers", "Kilometres", "Miles")
for items in range(1, 11):
    item = items*5 + 15
    print("{0:<5.1f} {1:<10.3f} {2:<10.1f} {3:<5.3f}".format(items, items*1.609, item, item/1.609))
