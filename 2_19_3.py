import sys


from mymod_2_19_3.mymod import count_lines, count_chars, test


string = sys.argv
if len(string) > 1:
    name_file = string[1]
else:
    name_file = input("Name file: ")


test(name_file)

