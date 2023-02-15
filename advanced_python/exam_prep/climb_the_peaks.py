from collections import deque

conquered_peaks = []
food_portions = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
day = 0
dict_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

while True:
    day += 1
    if day == 7:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    if not dict_peaks:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        if conquered_peaks:
            print("Conquered peaks:")
            print(*conquered_peaks, sep='\n')
        break

    daily_consumption = food_portions.pop() + stamina.popleft()
    if daily_consumption >= dict_peaks[0][1]:
        conquered_peaks.append(dict_peaks.popleft()[0])


