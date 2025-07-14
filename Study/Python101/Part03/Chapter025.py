'''
# Decorators

def another_function(func):
    """
    A function that accepts another function
    """
    def other_func():
        val = "The result of %s is %s" % (func(), eval(func()))
        return val
    return other_func

# A Simple Function
@another_function
def a_function():
    """A pretty useless function"""
    return 1+1

if __name__ == '__main__':
    value = a_function()
    print(value)
'''

'''
# Creating a Logging Decorator

import logging

def log(func):
    """
    Log what function is called
    """
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # add file handler
        fh = logging.FileHandler(".\Python_study_re\Python101\Part03\data\%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Running function: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func
    return wrap_log

@log
def double_function(a):
    """
    Double the input parameter
    """
    return a*2

if __name__ == "__main__":
    value = double_function(2)
'''

'''
# Built-in Decorators

# @classmethod and @staticmethod
class DecoratorTest(object):
    """
    Test regular method vs @classmethod vs @staticmethod
    """
    def __init__(self):
        """Constructor"""
        pass

    def doubler(self, x):
        """"""
        print("running doubler")
        return x * 2
    
    @classmethod
    def class_tripler(klass, x):
        """"""
        print("running tripler: %s" % klass)
        return x * 3
    
    @staticmethod
    def static_quad(x):
        """"""
        print("running quad")
        return x * 4
    
if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))

    print("")
    
    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)
'''

'''
# Python properties

class Person(object):
    """"""
    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """
        Return the full name
        """
        return "%s %s" %(self.first_name, self.last_name)
person = Person("Mike", "Driscoll")
print(person.full_name)
print(person.first_name)
print(person.last_name)
print("")
person.first_name = "Dan"
print(person.full_name)
'''

'''
# Replacing Setters and Getters with a Python property

from decimal import Decimal

class Fees(object):
    """"""
    def __init__(self):
        """Constructor"""
        self._fee = None

    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee
    
    def set_fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self_fee = value
f= Fees()
f.set_fee("1")
print(f.get_fee())
'''

'''
from decimal import Decimal

class Fees(object):
    """"""

    def __init__(self):
        """Constructor"""
        self._fee = None

    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee
    
    def set_fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)

f = Fees()
f.set_fee("1")
print(f.fee)
f.fee = "2"
print(f.get_fee())
'''

from decimal import Decimal

class Fees(object):
    """"""
    
    def __init__(self):
        """Constructor"""
        self._fee = None

    @property
    def fee(self):
        """
        The fee property - the getter
        """
        return self._fee
    
    @fee.setter
    def fee(self, value):
        """
        The setter of the fee property
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

if __name__ == '__main__':
    f = Fees()