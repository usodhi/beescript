import fbchat
from getpass import getpass
username = input("Username: ")
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))

beeMovie = open("colt45.txt")

text = beeMovie.read()

beeMovie.close()

for i in range(no_of_friends):
    name = input("Name: ")
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    #msg = input("Message: ")

    wordToSend = ''
    for word in text:
        if word == ' ' or word == "\n":
            sent = client.sendMessage(wordToSend, thread_id=friend.uid)
            wordToSend = ''
        else:
            wordToSend += word
            # if word == text[len(text) - 1]:
            #     sent=client.sendMessage(wordToSend, thread_id=friend.uid)

if sent:
    print("Message sent successfully!")