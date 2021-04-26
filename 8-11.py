def send_messages(text_message, sent_messages):
    while text_message:
        msg = text_message.pop()
        print(f"text in text_message: {msg} ")
        sent_messages.append(msg)
    for text in sent_messages:
        print(text)


msg_1 = ['hi', 'hello', 'gm']
sent_message = []
send_messages(msg_1[:], sent_message)
print(msg_1)
print(sent_message)