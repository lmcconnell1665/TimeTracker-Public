import pandas as pd
import re
from textblob import TextBlob

fct_entries = pd.read_csv("fct_entries.csv")
dim_tags = pd.read_csv("dim_tags2020-11-11 23:00:32.681432.csv")

#Select the tag you want to see
# key_id = dim_tags[dim_tags['label'] == 'Barr']['id'].values
# regex_string = '<{{\|t\|' + str(key_id[0]) + '\|}}>'
# fct_entries[fct_entries['note'].str.contains(regex_string)==True]

# Report the polarity of every time entry
for i in range(len(fct_entries)):
    blob = TextBlob(str(fct_entries['note'][i]))
    fct_entries['polarity'][i] = blob.sentiment.polarity


