list = input("Enter any text here: ")

def reverce(list):
    list = list.split()
    list.reverse()
    for i in list:
        print(i, end=' ')


reverce(list)