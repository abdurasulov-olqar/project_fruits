def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    data = data.split('\n')
    total = 0
    for i in data[1:-1]:
        total += float(i.split(',')[1])
    return total

f = open('fruits.csv').read()
print(get_total_price(f))


    