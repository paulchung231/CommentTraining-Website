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

csv_to_sample_from = argv[1] if len(argv) > 1 else "NYT_comments.csv"
path_to_data = "../Datasets/" + csv_to_sample_from
path_to_sampled = "./Output/"
comments_text_file = os.path.join(path_to_sampled, "Comments.txt")
replies_text_file = os.path.join(path_to_sampled, "Replies.txt")
data = pd.read_csv(path_to_data, header=None, usecols=[DataType.Comment.value, DataType.CommentType.value, DataType.UserName.value])

#data is now a 2d numpy array
data = data.values

#output files to store comments/replies
comments_file = open(comments_text_file, "w+")
replies_file = open(replies_text_file, "w+")

num_comments = 0
num_replies = 0
for i in range(data.shape[0]):
    if data[i][1] == "comment":
        comments_file.write(str(num_comments) + "\n" + str(data[i][0]) + "\n\n")
        num_comments += 1
    elif data[i][1] == "userReply":
        replies_file.write(str(num_replies) + "\n" + str(data[i][0]) + "\n\n")
        num_replies += 1

comments_file.close()
replies_file.close()
