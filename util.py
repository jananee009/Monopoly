def printmessage(message):
    print(message)
    with open('monopoly.log', 'a') as the_file:
        the_file.write(message + '\n')
