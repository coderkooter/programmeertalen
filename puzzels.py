def opgave1(mylist):
    return [i for i in range (1, len(mylist) + 1)] == sorted(mylist)

def opgave2(mylist):
    not_in_list = [i for i in range (1, len(mylist) + 1) if i not in mylist]
    for number in not_in_list:
        yield number

def opgave3a(filename):
    all_numbers = []

    with open(filename) as f:
        for line in f:
            res = [eval(i) for i in line.strip().split(" ")]
            all_numbers.append(res)

    return all_numbers

def opgave3b(mylist):
    for row in mylist:
        print(*row)

def opgave3(filename):
    opgave3b( opgave3a( filename ) )

def sum_nested_it(mylist):
    sum = 0

    while mylist:
        number = mylist.pop()
        if isinstance(number, int):
            sum += number
        else:
            for elem in number:
                mylist.append(elem)
    return sum
