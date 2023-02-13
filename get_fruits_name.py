def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    data = data.split('\n')
    l = []
    for i in data[1:-1]:
        l.append(i.split(',')[0])
    return l

f = open('fruits.csv').read()
print(get_frutis_name(f))

    