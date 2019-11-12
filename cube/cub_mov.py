#  1 Move TOP FURTHER SIDE to the RIGHT => Where F5 (back) is impacted
def lat_right_mov012(f1, f2, f3, f4, f5):

    f1_ori = f1[:]
    f2_ori = f2[:]
    f3_ori = f3[:]
    f4_ori = f4[:]
    f5_ori = f5[:]


    f1[0] = f4_ori[0]
    f1[1] = f4_ori[1]
    f1[2] = f4_ori[2]


    f2[0] = f1_ori[0]
    f2[1] = f1_ori[1]
    f2[2] = f1_ori[2]

    f3[0] = f2_ori[0]
    f3[1] = f2_ori[1]
    f3[2] = f2_ori[2]

    f4[0] = f3_ori[0]
    f4[1] = f3_ori[1]
    f4[2] = f3_ori[2]

    f5[0] = f5_ori[6]
    f5[3] = f5_ori[7]
    f5[6] = f5_ori[8]
    f5[1] = f5_ori[3]
    f5[7] = f5_ori[5]
    f5[2] = f5_ori[0]
    f5[5] = f5_ori[1]
    f5[8] = f5_ori[2]

    return f1, f2, f3, f4, f5

#  2 Move TOP FURTHER SIDE to the LEFT
def lat_left_mov012(f1, f2, f3, f4):

    f1_ori = f1[:]
    f2_ori = f2[:]
    f3_ori = f3[:]
    f4_ori = f4[:]


    f1[0] = f2_ori[0]
    f1[1] = f2_ori[1]
    f1[2] = f2_ori[2]


    f2[0] = f3_ori[0]
    f2[1] = f3_ori[1]
    f2[2] = f3_ori[2]

    f3[0] = f4_ori[0]
    f3[1] = f4_ori[1]
    f3[2] = f4_ori[2]

    f4[0] = f1_ori[0]
    f4[1] = f1_ori[1]
    f4[2] = f1_ori[2]

    return f1, f2, f3, f4

#  3 Move TOP MIDDLE to the RIGHT
def lat_right_mov345(f1, f2, f3, f4):

    f1_ori = f1[:]
    f2_ori = f2[:]
    f3_ori = f3[:]
    f4_ori = f4[:]


    f1[3] = f4_ori[3]
    f1[4] = f4_ori[4]
    f1[5] = f4_ori[5]


    f2[3] = f1_ori[3]
    f2[4] = f1_ori[4]
    f2[5] = f1_ori[5]

    f3[3] = f2_ori[3]
    f3[4] = f2_ori[4]
    f3[5] = f2_ori[5]

    f4[3] = f3_ori[3]
    f4[4] = f3_ori[4]
    f4[5] = f3_ori[5]

    return f1, f2, f3, f4

#  4 Move TOP MIDDLE to the LEFT
def lat_left_mov345(f1, f2, f3, f4):

    f1_ori = f1[:]
    f2_ori = f2[:]
    f3_ori = f3[:]
    f4_ori = f4[:]


    f1[3] = f2_ori[3]
    f1[4] = f2_ori[4]
    f1[5] = f2_ori[5]


    f2[3] = f3_ori[3]
    f2[4] = f3_ori[4]
    f2[5] = f3_ori[5]

    f3[3] = f4_ori[3]
    f3[4] = f4_ori[4]
    f3[5] = f4_ori[5]

    f4[3] = f1_ori[3]
    f4[4] = f1_ori[4]
    f4[5] = f1_ori[5]

    return f1, f2, f3, f4


#  5 Move TOP CLOSER SIDE to the RIGHT
def lat_right_mov678(f1, f2, f3, f4):

    f1_ori = f1[:]
    f2_ori = f2[:]
    f3_ori = f3[:]
    f4_ori = f4[:]


    f1[6] = f4_ori[6]
    f1[7] = f4_ori[7]
    f1[8] = f4_ori[8]

    f2[6] = f1_ori[6]
    f2[7] = f1_ori[7]
    f2[8] = f1_ori[8]

    f3[6] = f2_ori[6]
    f3[7] = f2_ori[7]
    f3[8] = f2_ori[8]

    f4[6] = f3_ori[6]
    f4[7] = f3_ori[7]
    f4[8] = f3_ori[8]

    return f1, f2, f3, f4


#  6 Move TOP CLOSER SIDE to the LEFT
def lat_left_mov678(f1, f2, f3, f4):

    f1_ori = f1[:]
    f2_ori = f2[:]
    f3_ori = f3[:]
    f4_ori = f4[:]

    f1[6] = f2_ori[6]
    f1[7] = f2_ori[7]
    f1[8] = f2_ori[8]

    f2[6] = f3_ori[6]
    f2[7] = f3_ori[7]
    f2[8] = f3_ori[8]

    f3[6] = f4_ori[6]
    f3[7] = f4_ori[7]
    f3[8] = f4_ori[8]

    f4[6] = f1_ori[6]
    f4[7] = f1_ori[7]
    f4[8] = f1_ori[8]

    return f1, f2, f3, f4


# 7 MOVE TOP LEFT side TOWARD self
def front_forward_mov036(f1, f6, f3, f5):

    f1_ori = f1[:]
    f6_ori = f6[:]
    f3_ori = f3[:]
    f5_ori = f5[:]

    f1[0] = f5_ori[0]
    f1[3] = f5_ori[3]
    f1[6] = f5_ori[6]

    f6[0] = f1_ori[0]
    f6[3] = f1_ori[3]
    f6[6] = f1_ori[6]

    f3[0] = f6_ori[0]
    f3[3] = f6_ori[3]
    f3[6] = f6_ori[6]

    f5[0] = f3_ori[0]
    f5[3] = f3_ori[3]
    f5[6] = f3_ori[6]

    return f1, f6, f3, f5


# 8 MOVE TOP LEFT side AWAY self
def front_backward_mov036(f1, f6, f3, f5):

    f1_ori = f1[:]
    f6_ori = f6[:]
    f3_ori = f3[:]
    f5_ori = f5[:]

    f1[0] = f6_ori[0]
    f1[3] = f6_ori[3]
    f1[6] = f6_ori[6]

    f6[0] = f3_ori[0]
    f6[3] = f3_ori[3]
    f6[6] = f3_ori[6]

    f3[0] = f5_ori[0]
    f3[3] = f5_ori[3]
    f3[6] = f5_ori[6]

    f5[0] = f1_ori[0]
    f5[3] = f1_ori[3]
    f5[6] = f1_ori[6]

    return f1, f6, f3, f5

# 9 MOVE TOP MIDDLE TOWARD self
def front_forward_mov147(f1, f6, f3, f5):

    f1_ori = f1[:]
    f6_ori = f6[:]
    f3_ori = f3[:]
    f5_ori = f5[:]

    f1[1] = f5_ori[1]
    f1[4] = f5_ori[4]
    f1[7] = f5_ori[7]

    f6[1] = f1_ori[1]
    f6[4] = f1_ori[4]
    f6[7] = f1_ori[7]

    f3[1] = f6_ori[1]
    f3[4] = f6_ori[4]
    f3[7] = f6_ori[7]

    f5[1] = f3_ori[1]
    f5[4] = f3_ori[4]
    f5[7] = f3_ori[7]

    return f1, f6, f3, f5


# 10 MOVE TOP MIDDLE AWAY from self
def front_backward_mov147(f1, f6, f3, f5):
    f1_ori = f1[:]
    f6_ori = f6[:]
    f3_ori = f3[:]
    f5_ori = f5[:]

    f1[1] = f6_ori[1]
    f1[4] = f6_ori[4]
    f1[7] = f6_ori[7]

    f6[1] = f3_ori[1]
    f6[4] = f3_ori[4]
    f6[7] = f3_ori[7]

    f3[1] = f5_ori[1]
    f3[4] = f5_ori[4]
    f3[7] = f5_ori[7]

    f5[1] = f1_ori[1]
    f5[4] = f1_ori[4]
    f5[7] = f1_ori[7]

    return f1, f6, f3, f5


# 11 MOVE TOP RIGHT side TOWARD self
def front_forward_mov258(f1, f6, f3, f5):

    f1_ori = f1[:]
    f6_ori = f6[:]
    f3_ori = f3[:]
    f5_ori = f5[:]

    f1[2] = f5_ori[2]
    f1[5] = f5_ori[5]
    f1[8] = f5_ori[8]

    f6[2] = f1_ori[2]
    f6[5] = f1_ori[5]
    f6[8] = f1_ori[8]

    f3[2] = f6_ori[2]
    f3[5] = f6_ori[5]
    f3[8] = f6_ori[8]

    f5[2] = f3_ori[2]
    f5[5] = f3_ori[5]
    f5[8] = f3_ori[8]

    return f1, f6, f3, f5


# 12 MOVE TOP RIGHT AWAY from self
def front_backward_mov258(f1, f6, f3, f5):

    f1_ori = f1[:]
    f6_ori = f6[:]
    f3_ori = f3[:]
    f5_ori = f5[:]

    f1[2] = f6_ori[2]
    f1[5] = f6_ori[5]
    f1[8] = f6_ori[8]

    f6[2] = f3_ori[2]
    f6[5] = f3_ori[5]
    f6[8] = f3_ori[8]

    f3[2] = f5_ori[2]
    f3[5] = f5_ori[5]
    f3[8] = f5_ori[8]

    f5[2] = f1_ori[2]
    f5[5] = f1_ori[5]
    f5[8] = f1_ori[8]

    return f1, f6, f3, f5



# 13 ROTATE TOP FIRST lateral side RIGHT => HEADACHE
def rotate_right_top_mov258_012_630_876(f4, f6, f2, f5):

    f4_ori = f4[:]
    f6_ori = f6[:]
    f2_ori = f2[:]
    f5_ori = f5[:]

    f4[2] = f5_ori[8]
    f4[5] = f5_ori[7]
    f4[8] = f5_ori[6]

    f6[0] = f4_ori[2]
    f6[1] = f4_ori[5]
    f6[2] = f4_ori[8]

    f2[6] = f6_ori[0]
    f2[3] = f6_ori[1]
    f2[0] = f6_ori[2]

    f5[8] = f2_ori[6]
    f5[7] = f2_ori[3]
    f5[6] = f2_ori[0]

    return f4, f6, f2, f5

# 14 ROTATE TOP FIRST lateral side LEFT => HEADACHE
def rotate_left_top_mov258_012_630_876(f4, f6, f2, f5):

    f4_ori = f4[:]
    f6_ori = f6[:]
    f2_ori = f2[:]
    f5_ori = f5[:]

    f4[2] = f6_ori[0]
    f4[5] = f6_ori[1]
    f4[8] = f6_ori[2]

    f6[0] = f2_ori[6]
    f6[1] = f2_ori[3]
    f6[2] = f2_ori[0]

    f2[6] = f5_ori[8]
    f2[3] = f5_ori[7]
    f2[0] = f5_ori[6]

    f5[8] = f4_ori[2]
    f5[7] = f4_ori[5]
    f5[6] = f4_ori[8]

    return f4, f6, f2, f5


# 15 ROTATE SECOND lateral side RIGHT
def rotate_right_center_mov147_345_741_543(f4, f6, f2, f5):

    f4_ori = f4[:]
    f6_ori = f6[:]
    f2_ori = f2[:]
    f5_ori = f5[:]

    f4[1] = f5_ori[5]
    f4[4] = f5_ori[4]
    f4[7] = f5_ori[3]

    f6[3] = f4_ori[1]
    f6[4] = f4_ori[4]
    f6[5] = f4_ori[7]

    f2[7] = f6_ori[3]
    f2[4] = f6_ori[4]
    f2[1] = f6_ori[5]

    f5[5] = f2_ori[7]
    f5[4] = f2_ori[4]
    f5[3] = f2_ori[1]

    return f4, f6, f2, f5


# 16 ROTATE SECOND lateral side LEFT
def rotate_left_center_mov147_345_741_543(f4, f6, f2, f5):

    f4_ori = f4[:]
    f6_ori = f6[:]
    f2_ori = f2[:]
    f5_ori = f5[:]

    f4[2] = f6_ori[0]
    f4[5] = f6_ori[1]
    f4[8] = f6_ori[2]

    f6[3] = f2_ori[7]
    f6[4] = f2_ori[4]
    f6[5] = f2_ori[1]

    f2[1] = f5_ori[3]
    f2[4] = f5_ori[4]
    f2[7] = f5_ori[5]

    f5[5] = f4_ori[1]
    f5[4] = f4_ori[4]
    f5[3] = f4_ori[7]

    return f4, f6, f2, f5


# 17 ROTATE BOTTOM THIRD lateral side right
def rotate_right_bottom_mov036_678_852_210(f4, f6, f2, f5):

    f4_ori = f4[:]
    f6_ori = f6[:]
    f2_ori = f2[:]
    f5_ori = f5[:]

    f4[0] = f5_ori[2]
    f4[3] = f5_ori[1]
    f4[6] = f5_ori[0]

    f6[6] = f4_ori[0]
    f6[7] = f4_ori[3]
    f6[8] = f4_ori[6]

    f2[8] = f6_ori[6]
    f2[5] = f6_ori[7]
    f2[2] = f6_ori[8]

    f5[2] = f2_ori[8]
    f5[1] = f2_ori[5]
    f5[0] = f2_ori[2]

    return f4, f6, f2, f5


# 18 ROTATE BOTTOM THIRD lateral side left
def rotate_left_bottom_mov036_678_852_210(f4, f6, f2, f5):

    f4_ori = f4[:]
    f6_ori = f6[:]
    f2_ori = f2[:]
    f5_ori = f5[:]

    f4[6] = f6_ori[8]
    f4[3] = f6_ori[7]
    f4[0] = f6_ori[6]

    f6[8] = f2_ori[2]
    f6[7] = f2_ori[5]
    f6[6] = f2_ori[8]

    f2[2] = f5_ori[0]
    f2[5] = f5_ori[1]
    f2[8] = f5_ori[2]

    f5[0] = f4_ori[6]
    f5[1] = f4_ori[3]
    f5[2] = f4_ori[0]

    return f4, f6, f2, f5