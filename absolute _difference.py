tree_height= int(input("please enter the tree height:"))
spaces=tree_height-1
stump_space=tree_height-1
hash=1
while(tree_height!=0):
    for i in range(spaces):
        print(" ",end="")


    for i in range(hash):
        print("#",end="")

    spaces -= 1
    hash+=2
print(" ",end="")
for i in range(stump_space):
    print("#" , end="" )



