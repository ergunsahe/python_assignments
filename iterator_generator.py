
#----------- writing our for loop
""" number = [1,2,3,4,5]
friends = ['ahmet', 'mehmet','ayşe']

# for n in number:
#     print(n)
# for n in friends:
#     print(n)

def my_for_loop(my_iterable):
    my_iterator = iter(my_iterable)
    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            break

my_for_loop(number)
my_for_loop(friends) """


#--------------to show thirth power of given range numbers with iterator class


""" class CubeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.end:
            result = self.start ** 3
            self.start += 1
            return result
        else:
            raise StopIteration
        
cubed = CubeNumbers(0, 5)
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed)) """


#--------to show thirth power of given range numbers with generator 

""" cubed = (x**3 for x in range(0, 5))
print(type(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed)) """


#---------------fibonacci numbers with generator function

""" def fibo(limit):
    x = 0
    y = 1
    while x < limit:
        yield x
        x, y = y, x + y
        
my_fib = fibo(1000)
for fib in my_fib:
    print(fib) """
    

#-------------to show index and value together

""" friends = ['john', 'walter', 'henry']

# i = 0
# while i < len(friends):
#     v = friends[i]
#     print(i, v)
#     i += 1

# for n in range(len(friends)):
#     v = friends[n]
#     print(n, v)

for i, v in enumerate(friends):
    print(i, v) """