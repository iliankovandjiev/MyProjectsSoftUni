tail = input()
body = input()
head = input()
meerkat = [tail, body, head]
meerkat[0], meerkat[-1] = meerkat[-1], meerkat[0]
print(meerkat)
