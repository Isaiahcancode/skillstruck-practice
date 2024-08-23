treats = [ "popcorn", "popsicles", "soda", "chips", "cookies"]
treat_1 = input("enter a treat")
treat_2 = input("enter another treat")
treats.extend([treat_1]+[treat_2])
print(treats)