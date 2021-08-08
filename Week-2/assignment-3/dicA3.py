def avg(data):
    sum = 0
    avg = 0
    count = 0
    for key,value in data.items():
        for value2 in value:
            sum += value2["price"]
            count += 1
    avg = round(sum/count, 3)
    return avg


print(
    avg({
        "products": [
            {
            "name": "Product 1",
            "price": 100
            },
            {
            "name": "Product 2",
            "price": 700
            },
            {
            "name": "Product 3",
            "price": 300
            }
        ]
    })
) # print the average price of all products (round to 3 decimal)