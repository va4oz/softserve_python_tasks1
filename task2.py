elem1 = input("enter element 1: ")
int_elem1 = int(elem1)
print("you entered ", elem1)

elem2 = input("enter element 2: ")
int_elem2 = int(elem2)
print("you entered ", elem2)

elem3 = input("enter element 3: ")
int_elem3 = int(elem3)
print("you entered ", elem3)

elem4 = input("enter element 4: ")
int_elem4 = int(elem4)
print ("you entered ", elem4)

elem5 = input("enter element 5: ")
int_elem5 = int(elem5)
print("you entered ", elem5)

list = [int_elem1, int_elem2, int_elem3, int_elem4, int_elem5]
print(list)

def summa(list):
    print("sum of all elements in list is ", sum(list))

summa(list)

def multily(list):
    mult = 1
    for i in list:
        mult = mult * i
    return mult

print("multiplies of all elements in list is ", multily(list))

