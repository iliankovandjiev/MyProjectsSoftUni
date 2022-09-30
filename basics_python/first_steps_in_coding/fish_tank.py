lenght_aqua = int(input())
width_aqua = int(input())
height_aqua = int(input())
porcent_aqua = float(input())
volume_aqua = lenght_aqua * width_aqua * height_aqua
volume_l = volume_aqua / 1000
ocupped_space = porcent_aqua / 100
litre_needed = volume_l - volume_l * ocupped_space
print(litre_needed)
