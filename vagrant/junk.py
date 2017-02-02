def outer(func):
    def inner():
        return func() + 1
    return inner

def get_num():
    return 2

class Momento:
   def __init__(self, x, y):
       self.x = x
       self.y = y

   def deco2(self, txt):
       def call(func):
           return func
       return call

   def __repr__(self):
       return "Momento(x={x}, y={y})".format(x=self.x, y=self.y)

   def __str__(self):
       return "{sum}".format(sum=self.x + self.y)

foo = outer(get_num)
print  foo()
foo = outer(foo)
print foo()
foo = outer(foo)
print foo()

new = Momento(5, 3)
print new
print repr(new)

def deco(func):
    def call():
        return func() + 4
    return  call

@deco
def to_deco():
    return 3

print 'decarada', to_deco()

@new.deco2('texto')
def nola():
    return 6

print 'otra decorada', nola()

class Etc:
    def __init__(self, n):
       self.n = n

    def print2(self, n):
        self._n = n
        print self._n, self.n
    n = property(print2)

etc = Etc(33)
print etc.n
etc.n=15
print etc.n

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius(55)
print c.temperature
c.temperature = 66