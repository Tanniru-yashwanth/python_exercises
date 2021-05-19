"""Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message."""


def show_messages(text_1):
    for msgs in text_1:
        print(msgs)


text = ['hi', 'hello', 'welcome', 'thank you']
show_messages(text)
