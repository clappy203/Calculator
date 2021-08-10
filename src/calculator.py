from numbers import Number


class Calculator:
      
    def __init__(self):
        self.__memory = 0

    def __evaluate_input (self, a: Number) -> Number:
        """ Takes only float or int data types 
        and throws up the error message not a number if it recieves any other datatype.
        :param a: any number of type int or float
        :return : returns the result of the value entered in a"""
        if not isinstance(a,(Number)):
            raise TypeError("Not a number")

    def add (self, a: Number) -> Number:
        """ Takes in a number n and returns the value after adding it to calculator memory.
        :param a: any number of type int or float
        :return : returns the result of the value entered in a """
        self.__evaluate_input(a)
        self.__memory += a
        return self.__memory 

    def reset (self):
        """ Clears up the memory and returns the number zero.
        :param a: any number of type int or float
        :return : returns the result of the value entered in a """
        self.__memory = 0 
        return self.__memory 

    def subtract (self, a: Number) -> Number:
        """Takes in a number n and subtracts n from memory.
        :param a: any number of type int or float
        :return : returns the result of the value entered in a"""
        self.__evaluate_input(a)
        self.__memory -= a
        return self.__memory 

    def multiply (self, b: Number) -> Number:
        """ Takes in a number n and multiply n by the number in memory.
        :param b: any number of type int or float
        :return : returns the result of the value entered in b"""
        self.__evaluate_input(b)
        self.__memory *= b
        return self.__memory 

    def divide (self, b: Number) -> Number:
        """ Takes in a number n and divide n by the number in memory.
        :param b: any number of type int or float
        :return : returns the result of the value entered in b"""
        self.__evaluate_input(b)
        try:
            self.__memory /= b
            return self.__memory
        except ZeroDivisionError as e:
            raise ZeroDivisionError(f"Cannot be divided by zero {e}")

    def nth_root(self, k: Number) -> Number:
        """ Takes in a number n and return the nth root of the number in memory.
        :param k: any number of type int or float
        :return : returns the result of the value entered in k"""
        self.__evaluate_input(k)
        self.__memory = self.__memory**(1./k)
        return self.__memory