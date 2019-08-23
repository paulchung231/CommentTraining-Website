from sys import argv
import os
import pandas as pd
import numpy as np
import random
from datetime import datetime
from enum import Enum
from matplotlib import pyplot as plt
import operator

#Data types within the csv. Enumeration is the label of column and the value is the column number in the csv.
# Meaning of column numbers in the csv --
# 3: Actual Comment
# 7: comment or userReply
# 19: Commenter username
class DataType(Enum):
    Comment = 3
    CommentType = 7
    UserName = 19

def graphHistogram(freq_data, x_label, y_label, title):
    fig, ax = plt.subplots()
    ax.hist(freq_data, bins=50)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    image_file = title+'.png'
    fig.savefig(image_file, bbox_inches='tight')

def checkStartsWithQuestion(comment):
    pos_period = comment.find('.')
    pos_exclam = comment.find('!')
    pos_question = comment.find('?')

    if pos_question >= 0 and pos_question < pos_period and pos_question < pos_exclam:
        return True
    else:
        return False

csv_to_sample_from = argv[1] if len(argv) > 1 else "NYT_comments.csv"
path_to_data = "../Datasets/" + csv_to_sample_from
path_to_sampled = "./Output/"
start_with_question_text_file = os.path.join(path_to_sampled, "Start_With_Question.txt")
data = pd.read_csv(path_to_data, header=None, usecols=[DataType.Comment.value, DataType.CommentType.value, DataType.UserName.value])

#data is now a 2d numpy array
data = data.values

#output files to store comments/replies
start_with_question_text_file = open(start_with_question_text_file, "w+")
character_frequencies_total = {}
character_frequencies_inital_comments = {}
character_frequencies_replies = {}

count = 0
total_comments_with_question = 0
total_start_with_question = 0

count_init = 0
init_comments_with_question = 0
init_start_with_question = 0

count_reply = 0
reply_comments_with_question = 0
reply_start_with_question = 0


for i in range(data.shape[0]):
    count += 1
    curr_char_count = len(data[i][0])
    curr_comment = data[i][0]
    question_in_comment = False
    start_with_question = False
    if '?' in curr_comment:
        if checkStartsWithQuestion(str(curr_comment)):
            start_with_question_text_file.write(str(count) + "\n" + str(curr_comment) + "\n\n")
            total_start_with_question += 1
            start_with_question = True

        total_comments_with_question += 1
        question_in_comment = True

    if curr_char_count not in character_frequencies_total:
        character_frequencies_total[curr_char_count] = 1
    else:
        character_frequencies_total[curr_char_count] += 1

    if data[i][1] == "comment":
        if question_in_comment:
            init_comments_with_question += 1

        if start_with_question:
            init_start_with_question += 1

        count_init += 1

        if curr_char_count not in character_frequencies_inital_comments:
            character_frequencies_inital_comments[curr_char_count] = 1
        else:
            character_frequencies_inital_comments[curr_char_count] += 1

    elif data[i][1] == "userReply":
        if question_in_comment:
            reply_comments_with_question += 1

        if start_with_question:
            reply_start_with_question += 1

        count_reply += 1

        if curr_char_count not in character_frequencies_replies:
            character_frequencies_replies[curr_char_count] = 1
        else:
            character_frequencies_replies[curr_char_count] += 1

freq_total = np.sort(np.array(list(character_frequencies_total.values())))
freq_init = np.sort(np.array(list(character_frequencies_inital_comments.values())))
freq_reply = np.sort(np.array(list(character_frequencies_replies.values())))

print("-------------------------------------------------------------------")
print("All Comments")
print("Total number of Comments: ", count)
print("Mean Character Count Total: ", np.mean(freq_total))
print("Standard Deviation Character Count Total: ", np.std(freq_total))
print("Mode of Character Counts: ", max(character_frequencies_total.items(), key=operator.itemgetter(1))[0])
print("Percentage with a Question: ", "{0:.2f}%".format((total_comments_with_question/count)*100))
print("Percentage of all that start with a Question: ", "{0:.2f}%".format((total_start_with_question/count)*100))
print("-------------------------------------------------------------------")
print("Initial Comments")
print("Total number of Initial Comments: ", count_init)
print("Mean Character Count Initial Comments: ", np.mean(freq_init))
print("Standard Deviation Character Count Initial Comments: ", np.std(freq_init))
print("Mode of Character Counts: ", max(character_frequencies_inital_comments.items(), key=operator.itemgetter(1))[0])
print("Percentage with a Question: ", "{0:.2f}%".format((init_comments_with_question/count_init)*100))
print("Percentage of all that start with a Question: ", "{0:.2f}%".format((init_start_with_question/count_init)*100))
print("-------------------------------------------------------------------")
print("Reply Comments")
print("Total number of Replies: ", count_reply)
print("Mean Character Count Replies: ", np.mean(freq_reply))
print("Standard Deviation Character Count Replies: ", np.std(freq_reply))
print("Mode of Character Counts: ", max(character_frequencies_replies.items(), key=operator.itemgetter(1))[0])
print("Percentage with a Question: ", "{0:.2f}%".format((reply_comments_with_question/count_reply)*100))
print("Percentage of all that start with a Question: ", "{0:.2f}%".format((reply_start_with_question/count_reply)*100))
print("-------------------------------------------------------------------")
print("")

graphHistogram(freq_total, 'Character Counts', 'Frequencies', 'Distribution of Character Counts on All Comments')
graphHistogram(freq_init, 'Character Counts', 'Frequencies', 'Distribution of Character Counts on Initial Comments')
graphHistogram(freq_reply, 'Character Counts', 'Frequencies', 'Distribution of Character Counts on Replies')

start_with_question_text_file.close()
