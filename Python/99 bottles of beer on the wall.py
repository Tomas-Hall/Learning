#total = 99
#while total > 0:
#    for x in range(0,2):
#        if total == 1:
#            print("%d bottle of beer on the wall" % total)
#        else:
#            print("%d bottles of beer on the wall" % total)
#    total -= 1
#    if total == 1:
#        print("take one down pass it around, %d bottle of beer on the wall" % total)
#    else:
#        print("take one down pass it around, %d bottles of beer on the wall" % total)

# original program in comments, decided to recursive function this up since i did the powershell one.
def second_function(bottles):
    return ("%d " % bottles) + ('bottles' if bottles != 1 else 'bottle')
def first_funtion(bottles):
    if bottles == 0:
        return
    result = second_function(bottles)
    print("%s of beer on the wall, %s of beer." % (result, result))
    bottles -= 1
    result = second_function(bottles)
    print("Take one down and pass it around, %s of beer on the wall." % result)
    first_funtion(bottles)

first_funtion(100)