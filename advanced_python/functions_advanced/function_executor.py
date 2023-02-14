def func_executor(*args):
    result = []

    for func, arg in args:
        result.append(f"{func.__name__} - {func(*arg)}")

    return "\n".join(result)

