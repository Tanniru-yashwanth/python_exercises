"""Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly."""


def send_messages(msgs):
    sent_messages = []
    while msgs:
        text = msgs.pop()
        sent_messages.append(text)
    print(msgs)
    print(sent_messages)


msgs_1 = ['hi', 'hello', 'welcome']

send_messages(msgs_1)
