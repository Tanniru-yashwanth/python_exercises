'''Start
with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages.After calling the function,
 print both of your list to show that the original list has retained its messages.'''


def send_messages(text_message):
    sent_messages = []
    while text_message:
        msg = text_message.pop()
        sent_messages.append(msg)
    print(text_message)
    print(sent_messages)


msg_1 = ['hi', 'hello', 'gm']
send_messages(msg_1[:])
print(msg_1)
