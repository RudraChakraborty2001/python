#return = statement used to end a function
#         and send a result back to the caller


def add(num1, num2):
    ans=num1+num2
    return ans

def subtract(num1,num2):
    ans=num1-num2
    return ans

def multiply(num1,num2):
    ans=num1*num2
    return ans

def divide(num1,num2):
    ans=num1/num2
    return ans

print(add(2,4))
print(subtract(2,4))
print(multiply(2,4))
print(divide(2,4))