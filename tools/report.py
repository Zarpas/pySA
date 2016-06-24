def printfile(fileobj):

    filecontents = fileobj.readlines()
    for content in filecontents:
        print(content[:-1])
    print('')
