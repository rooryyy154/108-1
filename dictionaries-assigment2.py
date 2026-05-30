market = {
    "fruit":"apple",
    "vegetable":"carrot",
    "merch":"chocholate"
}
print(market)

print(market["fruit"])

market["clothing"] = "Tshirt"
print(market)
print(len(market))

market["fruit"] = "orange"
print(market)
print(len(market))

market.pop("vegetable")
print(market)
print(len(market))