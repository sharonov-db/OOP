# Замыкание
def closure(x):
    def inner()
        return x + 3
    return inner
# d = 5
#  d() = 8



# Декоратор
def decorator(func):
    def wrapper(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result
    return wrapper

# @decorator
# def f(x):
#   return x ** 1234

# Если с @decorator - то добавится фразы before и after до и после числа при этом мы ссылаемся
# на функцию-декоратор
