def add(*args):
    sum=0 
    for n in args:
        sum += n
    return sum

print(add(3,5,6))

def calculate(**kwargs):
    print(kwargs)

    for key,value in kwargs.items():
       print(key)
       print(value)


calculate(add=3,multiply = 5)