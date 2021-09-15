import os
import segmentation
import keywords_num
import count_of_switch



root = "test.cpp"
words = segmentation.segment(root)
print("total num:",keywords_num.compute_num(words))
count_of_switch.count(words)
