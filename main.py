import os
import segmentation
import keywords_num
import count_of_switch



root = "test.cpp"
f = open(root,"r")
words = segmentation.segment(root)
print("total num:",keywords_num.compute_num(words))
