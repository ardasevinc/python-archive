import re
import pandas as pd
import matplotlib.pyplot as plt
import sys
import io
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

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

    # plt.show()
    plt.savefig('Rank.png', bbox_inches='tight', dpi=400)


def generate_one_time(dataframe):
    sorted_df = dataframe.sort_values(by='Count', ascending=False)
    final_df = sorted_df.drop_duplicates(subset='Sender', keep='first')
    final_df = final_df[['Count', 'Sender']]
    # final_df.plot.barh(x='Sender', y='Count', title='One time max', figsize=(8,14))

    # plt.savefig('One_time.png', bbox_inches='tight', dpi=400)


def generate_date_wcount(dataframe):
    sorted_df = dataframe.sort_values(by='Date', ascending=True)
    grouped_df = sorted_df.groupby(by='Date').sum()
    # grouped_df.plot(title='Date Word Count', color='Blue')

    # plt.savefig('D_count.png', bbox_inches='tight', dpi=400)
    

def generate_fahad(dataframe):
    # Generating Fahad day to day activity
    sorted_df = dataframe.sort_values(by='Date', ascending=True)
    is_Fahad = sorted_df['Sender'] == 'Fahad'
    sorted_df = sorted_df[is_Fahad]
    grouped_df = sorted_df.groupby(by='Date').sum()
    new_df = sorted_df.groupby(by='Date').cumsum()

    """grouped_df.plot.bar()
    plt.savefig('fahad1.png', dpi=400, bbox_inches='tight')
    grouped_df.plot()
    plt.savefig('fahad2.png', dpi=400, bbox_inches='tight')"""
    # new_df.plot()
    # plt.show()


def generate_time(dataframe):
    dataframe['Date'] = [get_day(df_date) for df_date in dataframe['Date']]
    dataframe['Time'] = [get_hour(df_time) for df_time in dataframe['Time']]
    grouped_df = dataframe.groupby(by=['Date', 'Time']).sum()
    grouped_df = grouped_df.sort_values(by='Count', ascending=True)

    pivoted_df = pd.pivot_table(
        data=grouped_df,
        values='Count',
        index='Date',
        columns='Time'
    )
    sns.heatmap(
        data=pivoted_df,
        linewidths=.2,
        cmap="YlGnBu"
    )

    plt.savefig('heatmap.png', dpi=400, bbox_inches='tight')


def generate_wordcloud(dataframe):
    split_text_data = dataframe['Message']
    joined_text = '\n'.join(split_text_data)
    wordcloud = WordCloud(background_color='white', width=1200, height=600, normalize_plurals=False, relative_scaling=0).generate(joined_text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('wordcloud.png', dpi=600)


def get_day(x_datetime):
    date_time_pattern = r"(\d+)/(\d+)/(\d+)"
    date_time_regex = re.compile(date_time_pattern)

    match_date = date_time_regex.search(x_datetime)
    if match_date is not None:
        return match_date.group(2)


def get_hour(x_time):
    time_pattern = r"(\d+):(\d+)"
    time_regex = re.compile(time_pattern)

    match_time = time_regex.search(x_time)
    if match_time is not None:
        return match_time.group(1)


print("Please make sure the export is in the same directory with the script\n")

try:
    file_path = input("Enter the filename with extension: ")
except NameError:
    file_path = input("Enter the filename with extension: ")

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

print("Dataframe generated successfully")

plt.style.use('ggplot')

print("Generating plots")

# generate_most_active(df)
# generate_one_time(df)
# generate_date_wcount(df)
# generate_fahad(df)
# generate_time(df)
generate_wordcloud(df)

print("Plot generation is successful")
