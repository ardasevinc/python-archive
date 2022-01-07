import re
import pandas as pd
import matplotlib.pyplot as plt


def word_counter(x_line):
    matches = re.findall(word_pattern, x_line)
    if matches is not None:
        return len(matches)
    else:
        return 0


file = open("yes_gang.txt", 'r')
contents = file.read()
file.close()

media = "\s<Media omitted>"
deleted = "\sThis message was deleted"
datetime = "(\d+\/\d+\/\d+)(,\s)(\d+:\d+)(\s-\s)(.*?)(:)"
neg_datetime = "^(?!((\d+\/\d+\/\d+)(,\s)(\d+:\d+)(\s-\s)(.*?)(:))).*$"
word_pattern = '\w+'
neg_datetime_regex = re.compile(neg_datetime, re.MULTILINE)
deleted_regex = re.compile(deleted)
media_regex = re.compile(media)
datetime_regex = re.compile(datetime)

#contents = neg_datetime_regex.sub("", contents)
contents = deleted_regex.sub("", contents)
contents = media_regex.sub("", contents)

split_text = contents.splitlines()
new_text = []

for i in split_text:
    if i != "":
        if datetime_regex.sub("", i) != "":
            new_text.append(i)

text = []
time = []
date = []
name = []

for i in new_text:
    match = datetime_regex.search(i)
    if match is not None:
        date.append(match.group(1))
        if match.group(5) == 'Maiu the BOB':
            name.append("Maiu")
        else:
            name.append(match.group(5))
        time.append(match.group(3))
        text.append(datetime_regex.sub("", i))
    if match is None:
        try:
            text[len(text)-1] += str(i)
        except IndexError:
            pass

w_count = [word_counter(line) for line in text]

data = pd.DataFrame(data=name, columns=['Sender'])
data['Count'] = w_count
data['Date'] = date
data['Time'] = time
data['Message'] = text

grouped = data.groupby(by='Date').sum()
grouped.sort_values(by='Date', ascending=True, inplace=True)

plt.style.use('ggplot')
grouped.plot.bar(title='Total Word Count by Day', color='Blue')

plt.show()


# text_to_csv = data.to_csv("group.csv", index=False, quotechar='"')
