from sys import argv
import os
import pandas as pd
import numpy as np
import random
from datetime import datetime
from enum import Enum

#Data types within the csv. Enumeration is the label of column and the value is the column number in the csv.
# Meaning of column numbers in the csv --
# 3: Actual Comment
# 7: comment or userReply
# 19: Commenter username
class DataType(Enum):
    Comment = 3
    CommentType = 7
    UserName = 19

word_to_find = argv[1]
csv_to_sample_from = argv[2] if len(argv) > 2 else "NYT_comments.csv"
path_to_data = "../Datasets/" + csv_to_sample_from
path_to_sampled = "./Output/"
output_file = "Comments_with_Word_" + word_to_find + ".txt"
comments_with_word_text_file = os.path.join(path_to_sampled, output_file)
data = pd.read_csv(path_to_data, header=None, usecols=[DataType.Comment.value, DataType.CommentType.value, DataType.UserName.value])

#data is now a 2d numpy array
data = data.values

#output files to store comments/replies
comments_with_word_file = open(comments_with_word_text_file, "w+")

num_comments_with_word = 0
for i in range(data.shape[0]):
    if word_to_find in data[i][0]:
        comments_with_word_file.write(str(num_comments_with_word) + "\n" + str(data[i][0]) + "\n\n")
        num_comments_with_word += 1

comments_with_word_file.close()
