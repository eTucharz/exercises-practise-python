'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.
'''
# create dict
counter_dict = {}
# open file for read
with open('Training_01.txt') as open_file:
    # store reading line as line
    line = open_file.readline()
    # repeat as long as line exist
    while line:
        line = line[3:-26]  # slice category name from line
        if line in counter_dict:
            counter_dict[line] += 1  # increase value when key exist
        else:
            # create key and assign value when not exist
            counter_dict[line] = 1
        line = open_file.readline()  # read next line

print(counter_dict)  # print dict
