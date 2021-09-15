import os
import keywords_num

root = "test.cpp"

f = open(root,"r")
lines = f.readlines()

print("After segmentation:")
print("total num:", keywords_num.compute_num(lines))





