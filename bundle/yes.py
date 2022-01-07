import re

text_file = open("yes_gang.txt")
text = text_file.read()
text_file.close()

yes_pattern = "ye\w"
date_time_pattern = "(\d+\/\d+\/\d+,\s)(\d+:\d+)(\s-\s)(.*?)(:)"
media_pattern = "\s<Media omitted>"
word_pattern = "\w+"
test_pattern = "(\d+\/\d+\/\d+,\s)(\d+:\d+)(\s-\s)(.*?)(:)(\s<Media omitted>)?(\sThis message was deleted)?"
test_regex = re.compile(test_pattern)
date_time_regex = re.compile(date_time_pattern)
yes_regex = re.compile(yes_pattern)
word_regex = re.compile(word_pattern)
media_regex = re.compile(media_pattern)

word_count = [0, 0]
yes_count = {}

def word_counter(x_line):
    matches = re.findall(word_pattern, x_line)
    if matches is not None:
        return len(matches)
    else:
        return 0


text = media_regex.sub("", text)
line_count = 0
name = ""

for line1 in text.splitlines():
    match = test_regex.search(line1)
    if match is not None:
        name = match.group(4)
        #print(name)
        line_count += 1
        if name not in yes_count.keys():
            yes_count[name] = word_counter(line1)
        if name in yes_count.keys():
            yes_count[name] += word_counter(line1)
    if match is None:
        try:
            yes_count[name] += word_counter(line1)
            line_count += 1
        except KeyError:
            pass

keys = list(yes_count.keys())
vals = list(yes_count.values())

for i in range(len(vals)):
    print(keys[i] + ": " + str(vals[i]))


# text = test_regex.sub("", text)

"""
for line in text.splitlines():
    if line != "":
        word_count[0] += 1
        word_count[1] += len(re.findall(word_pattern, line))
        print(line)

print("\n")
print(word_count[0], word_count[1])
"""