import itertools


class SixteenTricks:

    def test(self):
        self.ternary_operator('ternary operator ', 15, 8)
        self.enumerate_function('enumerate function ', ['apple', 'banana', 'jack-fruits'])
        self.zip_function('zip function ')
        self.any_all_function('any all function ')
        self.list_comprehensions('list comprehensions ')
        self.lambda_function('lambda function ')
        self.itertools_('itertools ', [1, 2, 3])
        self.generate_fibonacci_series('generator ', 3)
        self.multiple_function_arguments('multiple arguments ')

    @staticmethod
    def ternary_operator(message, a, b):
        max_value = a if a > b else b
        print(message, max_value)

    @staticmethod
    def enumerate_function(message, fruits):
        for index, fruit in enumerate(fruits):
            print(message, index, fruit)

    @staticmethod
    def zip_function(message):
        list1 = [1, 3, 5]
        list2 = ['a', 'b']
        for x, y in zip(list2, list1):
            print(message, x, y)

    @staticmethod
    def list_comprehensions(message):
        cube_values = [x ** 3 for x in range(1, 6)]
        print(message, cube_values)

    @staticmethod
    def lambda_function(message):
        add_ = lambda value1, value2: value1 + value2
        print(message, add_(3, 5))

    @staticmethod
    def any_all_function(message):
        numbers = [1, 0, 3, 4]
        print(message, any(numbers))
        print(message, all(numbers))

    @staticmethod
    def itertools_(message, numbers):
        numbers_permutation = list(itertools.permutations(numbers))
        print(message, numbers_permutation)

    @staticmethod
    def generate_fibonacci_series(message, n):
        a, b = 0, 1
        for i in range(0, n):
            yield a
            a, b = b, a + b

    # decorators
    @staticmethod
    def decorators(message):
        def log_function(func):
            def wrapper(*args, **kwargs):
                print(message, f'function running {func.__name__}')
                result = func(*args, **kwargs)
                print(message, f'{func.__name__} returned result')
                return result

            return wrapper

        @log_function
        def add(a, b):
            return a + b

        print(add(6, 90))

    # multiple function arguments

    @staticmethod
    def multiple_function_arguments(message):
        def print_arguments(*args, **kwargs):
            print(message, args)
            print(message, kwargs)

        print_arguments(1, 2, 3, name="Md. Emran Hossain", age='28')
        result = {x: x ** 2 for x in range(1, 10)}
        print(message, result)


sixteen_tricks = SixteenTricks()
sixteen_tricks.test()
