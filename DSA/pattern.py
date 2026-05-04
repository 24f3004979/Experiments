
def pattern(size):
    number = 1
    for _ in range(size):
        string = '*' * number
        number += 1
        number = number ** 2
        print(string)

i = int(input("Enter Size for star :"))
pattern(i) 

