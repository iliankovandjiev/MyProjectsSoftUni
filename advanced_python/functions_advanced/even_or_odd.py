def even_odd(*args):
    result = []
    if args[-1] == "odd":
        for n in args[:-1]:
            if int(n) % 2 != 0:
                result.append(n)
    elif args[-1] == "even":
        for n in args[:-1]:
            if int(n) % 2 == 0:
                result.append(n)

    return result

