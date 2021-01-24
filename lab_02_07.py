n = int(input(),12)
print(n)

def convert(n):
    x = (n % 14)
    c = ""
    if (x < 10):
        c = x
    if (x == 10):
        c = "A"
    if (x == 11):
        c = "B"
    if (x == 12):
        c = "C"
    if (x == 13):
        c = "D"
        
    if (n - x != 0):
        return convert(n // 14) + str(c)
    else:
        return str(c)
 
print(convert(n))