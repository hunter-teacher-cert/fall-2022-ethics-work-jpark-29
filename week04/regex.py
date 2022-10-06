import re


def find_name(line):
    pattern = re.compile(r'[A-Z][a-z]*\.?\s?[A-Z]*[a-z]+')
    result = re.findall(pattern,line)
    return result


f = open("names.txt")

for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)