import re
with open('access_log', "r") as file:
    data = file.readlines()
    #counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    lv_200 = re.compile(r'(^([2][0][0]+)+$)')
    lv_400 = re.compile(r'(^([4][0][0]+)+$)')
    lv_404 = re.compile(r'(^([2][0][0]+)+$/)')
    for line in data:
        word = line.split()
        wordlist = word[8]
        #counter += 1
        #print(word)
        #print(wordlist)
        if lv_200.search(wordlist):
            counter1 += 1.
        elif lv_400.search(wordlist):
            counter2 += 1.
        elif lv_404.search(wordlist):
            counter3 += 1.
        else:
            counter4 += 1.
#print('Total Number of lines', counter)
print('Number of Failure Status Code for 200:', counter1)
print('Number of Failure Status Code for 400:', counter2)
print('Number of Failure Status Code for 404:', counter3)
print('Number of Success Status Code:', counter4)
        
