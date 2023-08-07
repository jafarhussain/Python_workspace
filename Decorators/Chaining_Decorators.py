def decorator1(func):
    def f():
        x = func()
        return x * x

    return f

def decorator2(func):
    def f():
        x = func()
        return x * 3

    return f

@decorator1
@decorator2
def n1():
    return 10

@decorator2
@decorator1
def n2():
    return 10

print(n1())
print(n2())


#The order in which the function gets called -  
# 
# decorator1(decorator2(n)) -> 10*3 -> 30*30
# decorator2(decorator1(n)) -> 10*10 -> 100*3



