from cub_var import *
from cub_mov import *




f1 = green
f2 = blue
f3 = white
f4 = orange
f5 = yellow
f6 = red

cube = [f1,         #  TOP
    f4, f6, f2, f5, #  LEFT, FRONT, RIGHT, BACK
        f3]         #  BOTTOM





print("ORIGINAL STATE")
print(f1, f2, f3, f4, f5)

test = lat_right_mov012(f1, f2, f3, f4, f5)

print("NEW STATE")
print(test)