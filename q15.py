# import spam
#
# spam.bacon()
# spam.eggs()

# from spam import bacon, eggs
#
# bacon()
# eggs()
#
def eggs():
    print("I have eggs.")


from spam import eggs as another_egg


eggs()
another_egg()
