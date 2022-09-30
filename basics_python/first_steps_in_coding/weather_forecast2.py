temperature = float(input())
if  temperature<=35 and temperature>=26:
    print("Hot")
elif temperature<26 and temperature>=20.1:
    print("Warm")
elif temperature<20.1 and temperature>=15:
    print("Mild")
elif temperature<15 and temperature>=12:
   print("Cool")
elif temperature<12 and temperature>=5:
    print("Cold")
else:
    print("unknown")
