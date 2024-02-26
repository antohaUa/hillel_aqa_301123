# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

a = [1, 2, 3]
try:
    print(f"Second element {a[1]}")
    # Throws error since there are only 3 elements in array
    # print("Fourth element = %d" % (a[3]))
    print(1 / 0)
    # raise ZeroDivisionError()
    # raise ValueError('1123')
except ArithmeticError as zd_err:
    print(zd_err)
    print('Zero Error was here')
except (IndexError, ValueError) as custom_err:
    print("Index error")
    print('Value Error catched')
except Exception as g_exc:
    print("Global error occurred:")
    print(g_exc)
finally:
    print("End of all")
