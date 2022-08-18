def countDown(x):
    for num in range(x, -1, -1):
        print(num)
print(countDown(5))

def printAndReturn(y):
    print(y[0])
    return(y[1])
print(printAndReturn([3,2]))

def firstPlusLength(z):
    product = z[0] + len(z)
    return(product)
numbers3 = [3,5,1,1,1,1]
print(firstPlusLength(numbers3))

def greaterThanSecond(c):
    product = []
    for num in range(0, len(c)):
        if(len(c) < 2):
            return False
        elif(c[1] <c[num]):
            product.append(c[num])
    return product
number4 = [2]
numbers4 = [3,4,1,5,2,7]
print(greaterThanSecond(numbers4))
print(greaterThanSecond(number4))

def lengthAndValue(v):
    product = []
    for v[0] in range(0, v[0]):
        product.append(v[1])
    return product
numbers5 = [5,2]
print(lengthAndValue(numbers5))