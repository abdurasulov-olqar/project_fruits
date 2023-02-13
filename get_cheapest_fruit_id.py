def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    data = data.split('\n')
    narxi = []
    for i in data[1:-1]:
        narxi.append(float(i.split(',')[1]))
    return narxi.index(min(narxi))

f = open('fruits.csv').read()
print(get_cheapest_fruit_id(f))