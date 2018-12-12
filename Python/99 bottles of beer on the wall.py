total = 99
while total > 0:
    for x in range(0,2):
        if total == 1:
            print("%d bottle of beer on the wall" % total)
        else:
            print("%d bottles of beer on the wall" % total)
    total -= 1
    if total == 1:
        print("take one down pass it around, %d bottle of beer on the wall" % total)
    else:
        print("take one down pass it around, %d bottles of beer on the wall" % total)
   
