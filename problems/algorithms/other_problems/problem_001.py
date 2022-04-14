def chain_sum(n):
    res = n

    def wrapper(n2=None):
        nonlocal res
        if n2 is None:
            return res
        res += n2
        return wrapper
    return wrapper


def chain_sum_02(n):
    def wrapper(n2=None):
        if n2 is None:
            return wrapper.res
        wrapper.res += n2
        return wrapper
    wrapper.res = n
    return wrapper


# w/o 'if'
def chain_sum_03(n):
    res = n

    def wrapper(n2=None):
        nonlocal res
        try:
            n2 = int(n2)
        except TypeError:
            return res
        res += n2
        return wrapper
    return wrapper


# w/o 'if' and 'try-except'
def chain_sum_04(n):
    def wrapper(n2=None):
        def inner():
            wrapper.res += n2
            return wrapper
        logic = {
            type(None): lambda: wrapper.res,
            int: inner
        }
        return logic[type(n2)]()
    wrapper.res = n
    return wrapper


if __name__ == '__main__':
    q = chain_sum_04(4)(9)() # return 13
    print(q)
