n, m = input().split()

first_set = set(input() for _ in range(int(n)))
second_set = set(input() for _ in range(int(m)))
print(*first_set.intersection(second_set), sep='\n')