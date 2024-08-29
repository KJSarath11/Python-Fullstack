from csv import reader
def read_csv():
    with open(r"D:\CODING\Pyspiders\Python-Fullstack\PYTHON\File Handling\Files\employee.csv") as f:
        records = []
        rows = reader(f)  # creating an instance of 'reader' function
        headers = next(f) # skipping first record
        expected_types = [str,str,int,str,str]
        for row in rows:
            converted = [expected_type(item) for expected_type,item in zip(expected_types,row)]
            records.append(converted)
    return records
       
# what is the total amount that i am paying to all employees as salary
def total_pay():
    # read the contents of csv file into python data-structure
    data = read_csv()
    _total_pay = 0
    for item in data:
        _total_pay = _total_pay + item[2]
    return _total_pay

#