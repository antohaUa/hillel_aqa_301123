# Given function that accepts positional arguments
# write decorator that will accept params strings_allowed=True/False
# and raise Assert Error in case unfulfilled condition

def deco_params(strings_allowed=True):
    def deco(func):
        def wrapper(*args):
            if not strings_allowed:
                if any(type(el) == str for el in args):
                    raise AssertionError('Strings are not allowed')
            print(f'{strings_allowed}')
            func(*args)

        return wrapper

    return deco


@deco_params(strings_allowed=False)
def target_function(*args):
    print(f'Working OK with {args=}')


# target_function(1, 2, 3, 5)
# target_function('a', 'b', 'c')
# target_function(1, 2, 3, 5)
target_function(1, 2, 4, 's', 8, 0)
