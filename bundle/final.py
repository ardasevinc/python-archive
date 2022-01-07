import re

# Functions below.


def word_counter(x_line):
    matches = re.findall(word_pattern, x_line)
    if matches is not None:
        return len(matches)
    else:
        return 0


def word_by_person():
    line_count = 0
    word_count = {}
    name = ""

    for line in text.splitlines():
        match = datetime_regex.search(line)
        if match is not None:
            name = match.group(7)
            # print(name)
            line_count += 1
            if name not in word_count.keys():
                word_count[name] = word_counter(line)
            if name in word_count.keys():
                word_count[name] += word_counter(line)
        if match is None:
            try:
                word_count[name] += word_counter(line)
                line_count += 1
            except KeyError:
                pass

    return word_count


def write_dict(x_dict, filename):
    keys = list(x_dict.keys())
    values = list(x_dict.values())

    f = open(filename, 'w+')

    for i in range(len(values)):
        f.write(keys[i] + ": " + str(values[i]) + "\n")
    f.close()


def word_avg_day():
    l_day, f_day, total = 0, 0, 0
    days = []
    split_text = text.splitlines()

    for i in range(len(split_text)):
        match = datetime_regex.search(split_text[i])
        if match is not None:
            days[i] = match.group(2)
        if match is None:
            if i != len(split_text)-1:
                days[i+1] = days[i]
            elif i == len(split_text)-1:
                days[i] = days[i-1]


    for i in range(len(split_text)):
        split_text[i] = datetime_regex.sub("", split_text[i])
        if (days[i] == days[i+1]) and (i != len(split_text)-1):
            total += word_counter(split_text[i])
        elif (days[i] != days[i+1]) and (i != len(split_text)-1):
            if days[i] == days[i-1]:
                total += word_counter(split_text[i])
        elif i == len(split_text)-1:
            total += word_counter(split_text[i])
            break

    return total / (days[len(split_text)-1] - days[0])

# End of functions


path = input("Please enter the filename and make sure you got the file as the same directory as the script:")
file = open(path)
text = file.read()
file.close()


print("Options")
print("1: Word count")
print("2: Avg words per day")
# Some other options here

selected = int(input())

datetime_regex = re.compile('(\d+)\/(\d+)\/(\d+)(,\s)(\d+:\d+)(\s-\s)(.*?)(:)')
media_regex = re.compile("\s<Media omitted>")
word_pattern = '\w+'

text = media_regex.sub("", text)  # Substituting media with an empty string

if selected == 1:

    output = word_by_person()
    write_dict(output, "stats.txt")


if selected == 2:

    avg_val = word_avg_day()
    print("Average per day is: ", avg_val)
