def create_file():
    open("monopoly.log", 'w').close()

def printmessage(message):
    print(message)
    with open('monopoly.log', 'a') as log_file:
        log_file.write(message + '\n')
