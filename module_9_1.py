def apply_all_func(int_list, *function):
    result = dict()
    for fun in function:
        result[fun.__name__] = fun(int_list)
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))