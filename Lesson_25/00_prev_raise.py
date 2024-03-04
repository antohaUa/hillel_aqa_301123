# def status(n):
#     return True if n > 5 else False
#
#
# print(status(5))
#
# # if approach
# if status(10) is True:
#     pass
# else:
#     pass


def status_exc(n):
    if n > 5:
        raise SystemError('Bad News')
    elif n < 3:
        raise ValueError('Wrong N')
    return True


# exceptions approach
try:
    #result = status_exc(10)
    print(status_exc(10))
except ValueError as v_err:
    print(v_err)
except Exception as g_exc:
    print(g_exc)
