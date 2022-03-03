with open('Training_01.txt', 'r') as open_file:
    # get content of file
    all_text = open_file.read()
    # split string to get list of names
    images_list = all_text.splitlines()

    # print(images_list)
    # for image in images_list:
    #  print(image.split('/')[2])

    names_repeats = {image.split(
        '/')[2]: images_list.count(image) for image in images_list}
    print(names_repeats)
