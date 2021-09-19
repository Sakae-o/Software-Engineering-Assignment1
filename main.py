import os
import segmentation
import keywords_num
import count_of_switch as cnt_s
import count_of_if_else as cnt_ie



print("Please input the path of a cpp file:", end=" ")
root = input()
print("Please input the execution level:", end=" ")
level = int(input())

words = segmentation.segment(root)
total_num = keywords_num.compute_num(words)
num_s, num_c = cnt_s.count(words)
num_i_e = cnt_ie.count_if_else(words)
num_i_e_e = cnt_ie.count_else(words) - num_i_e

if(level >= 1):
    print("total num:", total_num)
if(level >= 2):
    print("switch num:", num_s)
    print("case num:", end=" ")
    for c in num_c:
        print(c, end=" ")
if (level >= 3):
    print("\nif-else num:", num_i_e)
if(level == 4):
    print("if-elseif-else num:", num_i_e_e)




