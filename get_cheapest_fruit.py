def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    data = data.split('\n')
    meva = []
    narxi = []
    for i in data[1:-1]:
        meva.append(i.split(',')[0])
        narxi.append(float(i.split(',')[1]))
    return meva[narxi.index(min(narxi))]

f = open('fruits.csv').read()
print(get_cheapest_fruit(f))