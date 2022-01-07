import re
import pandas as pd
import matplotlib.pyplot as plt
import sys
import io


def word_counter(x_line):
    matches = re.findall(word_pattern, x_line)
    if matches is not None:
        return len(matches)
    else:
        return 0


def sub_regex(file_content):
    file_content = deleted_regex.sub("", file_content)
    file_content = media_regex.sub("", file_content)

    return file_content


def generate_most_active(dataframe):
    grouped_df = dataframe.groupby(by='Sender').sum()
    grouped_df.sort_values(by='Count', ascending=False, inplace=True)
    grouped_df.plot.bar(title='Rankings', color='Blue')

    plt.savefig('Rank.png', bbox_inches='tight', dpi=400)


def generate_one_time(dataframe):
    sorted_df = dataframe.sort_values(by='Count', ascending=False)
    final_df = sorted_df.drop_duplicates(subset='Sender', keep='first')
    final_df = final_df[['Count', 'Sender']]
    final_df.plot.barh(x='Sender', y='Count', title='One time max')

    plt.savefig('One_time.png', bbox_inches='tight', dpi=400)


def generate_date_wcount(dataframe):
    sorted_df = dataframe.sort_values(by='Date', ascending=False)
    grouped_df = sorted_df.groupby(by='Date').sum()
    grouped_df.plot.bar(title='Date Word Count', color='Blue')

    plt.savefig('D_count.png', bbox_inches='tight', dpi=400)


try:
    file_path = input("Enter the export path:")
except NameError:
    file_path = input("Enter the export path:")

try:
    with io.open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
except IOError as e:
    print("File " + file_path + " not found")
    sys.exit()

media = "\s<Media omitted>"
deleted = "\sThis message was deleted"
datetime = "(\d+\/\d+\/\d+)(,\s)(\d+:\d+)(\s-\s)(.*?)(:)"
# neg_datetime = "^(?!((\d+\/\d+\/\d+)(,\s)(\d+:\d+)(\s-\s)(.*?)(:))).*$"
word_pattern = '\w+'
# neg_datetime_regex = re.compile(neg_datetime, re.MULTILINE)
deleted_regex = re.compile(deleted)
media_regex = re.compile(media)
datetime_regex = re.compile(datetime)

mod_contents = sub_regex(contents).splitlines()
new_contents = []

for i in mod_contents:
    if i != "":
        if datetime_regex.sub("", i) != "":
            new_contents.append(i)


date = []
time = []
text = []
name = []

for i in new_contents:
    match = datetime_regex.search(i)

    if match is not None:
        date.append(match.group(1))
        name.append(match.group(5))
        time.append(match.group(3))
        text.append(datetime_regex.sub("", i))
    elif match is None:
        try:
            text[len(text)-1] += str(i)
        except IndexError:
            pass


word_count = [word_counter(line) for line in text]

df = pd.DataFrame(data=name, columns=['Sender'])

df['Count'] = word_count
df['Date'] = date
df['Time'] = time
df['Message'] = text

print("Dataframe established successfully")

plt.style.use('ggplot')

print("Generating plots")

generate_most_active(df)
generate_one_time(df)
generate_date_wcount(df)
