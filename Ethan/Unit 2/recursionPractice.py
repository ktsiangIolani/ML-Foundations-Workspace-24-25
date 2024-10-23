
def fibonacci(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    #recursive case
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(2))

def factorial(n):
    if n == 1:
        return 1
        
    return factorial(n-1) * n
    
print (factorial(999))
