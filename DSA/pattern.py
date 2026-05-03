def pattern(size):
    
    n = 1
    for row in range(size):
        s = "*" * n
        print(s)
        n += 1

i = int(input("Enter size for the star pattern"))
pattern(i)
