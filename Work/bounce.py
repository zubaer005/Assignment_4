# bounce.py
#
# Exercise 1.5
distance = 100
for i in range(1, 11, 1):
        new_distance = distance*(3/5)
        print (i, round(new_distance,4))
        distance=new_distance