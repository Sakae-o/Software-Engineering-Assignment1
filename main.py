import os
import segmentation
import keywords_num
import count_of_switch as cnt_s
import count_of_if_else as cnt_ie


root = "test_file/test.cpp"
words = segmentation.segment(root)
print("total num:",keywords_num.compute_num(words))
cnt_s.count(words)
print("\nif-else num:", cnt_ie.count(words))

