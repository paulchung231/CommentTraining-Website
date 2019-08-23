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

csv_to_sample_from = argv[1] if len(argv) > 2 else "NYT_comments.csv"
number_to_sample = int(argv[2]) if len(argv) > 2 else 200
print("Number of comments sampled:", number_to_sample)
path_to_data = "../Datasets/" + csv_to_sample_from
path_to_sampled = "./Output/"
complete_name = os.path.join(path_to_sampled, "Sampled_Comments.txt")

#To get "more" random numbers
random.seed(datetime.now())
data = pd.read_csv(path_to_data, header=None, usecols=[DataType.Comment.value, DataType.CommentType.value, DataType.UserName.value])

#random comments with replacement
# sampled_comments = random.choices(data[DataType.Comment.value], k=number_to_sample)

#random comments without replacement
sampled_comments = random.sample(list(data[DataType.Comment.value]), k=number_to_sample)

with open(complete_name, "w+") as file:
    for i, comment in enumerate(sampled_comments):
        file.write(str(i) + "\n" + str(comment) + "\n\n")
