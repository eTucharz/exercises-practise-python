'''
Given a .txt file that has a list of a bunch of names,
count how many of each name there are in the file,
and print out the results to the screen. I have a .txt file for you, if you want to use it!

'''
# open file for read
with open('nameslist.txt', 'r') as open_file:
    # get content of file
    all_text = open_file.read()
    # split string to get list of names
    names_list = all_text.splitlines()
    # get number of name's repeats using dict comprehensions
    names_repeats = {name: names_list.count(name) for name in names_list}
    # print dict
    print(names_repeats)
