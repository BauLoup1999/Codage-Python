import sys
import math



surface_n = int(input())  
for i in range(surface_n):
    
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()] # h speed = vitesse horizontal, v speed = vitesse vertical

    if v_speed < -40 and power < 4: #si la vitesse vertical est inférieur a -40, et que la vitesse est inférieur a 4 (qui est le maximum)
        power += 1 # alors on augmente la puissance de 1 pour ralentir la fusée


    print("0 "+str(power))
