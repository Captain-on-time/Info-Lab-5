print("Numbers < 10 (while):") 
i = 0 
while (i<10):     
    print(i, end=" ") 
    i += 1 
print("\n") 


print("Numbers < 10 (for):") 
for i in range(0,10):     
    print(i, end=" ") 
else:    
    print("\nThe next number is 10\n") 
 

sum = 0 
for i in range(0,100):     
    if i > 10:         
        print("\nWe reached the end, final sum: ", sum)         
        break     
    sum += i 
 
 
i = 0
while i<=15:     
    if i % 3 == 0:         
        i += 1         
        continue     
    print(i, end=" ")     
    i += 1 
 
print("\n") 
 

print("Let's print numbers again!") 
for i in range(0,10):     
    pass     
    print(i, end=" ") 
 
print("\n\n")


i=0    
while i<500:
    if (i%7 == 0 and i%2 == 1):
        print(i, end=" ")
    if i == 300:
        break
    i=i+1
else: 
    print("All numbers were printed!")

print("\n")

for i in range(0, 500):
    if (i%7 == 0 and i%2 == 1):
        print(i, end=" ")
    if i == 300:
        break
else: 
    print("All numbers were printed!")

print("\n\n")

for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            print(j, end=" ")
        else:
            print(0, end=" ")
    print("\n")

print("\n\n")

i = 1
while i < 5:
    j = 1
    while j < 5:
        if i == j:
            print(j, end=" ")
        else:
            print(0, end=" ")
        j += 1
    i += 1
    print("\n")