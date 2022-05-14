string = input()
lst = []
for i in range(len(string)):
    if(string[i] not in lst):
        if(string.count(string[i]) > 1):
            print("{}, count = {}".format(string[i], string.count(string[i])))
            lst.append(string[i])