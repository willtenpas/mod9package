def august_intelligence():
    from time import sleep
    index = int(input("Give an integer 1 to 100: "))
    index = index % 4
    intelligence_list = ['still kinda dumb', 'actually pretty smart', 'so so intelligent', "can't count to 10"]
    '''Tells you how smart August is'''
    print("Calculating August's intelligence")
    sleep(.2)
    print("...")
    sleep(.5)
    print("...")
    sleep(.2)
    print("Almost calculated")
    sleep(.3)
    print('...')
    sleep(.4)
    print("August {}".format(intelligence_list[index]))