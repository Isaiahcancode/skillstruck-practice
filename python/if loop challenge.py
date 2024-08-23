my_list = [int(x) for x in input("Input a list of numbers").split()]

for x in my_list:
if x == 0:	
    my_list = str(x)
    print(len(my_list))
