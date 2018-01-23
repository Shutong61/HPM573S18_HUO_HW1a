def sum(x):
    if x == 1:
        return 1
    else:
        return x+sum(x-1)
print (sum(100))

def sum_iter(y):
    sum = 0
    for i in range(1,y+1):
        sum +=i
    return sum
print (sum_iter(100))

