fishLength=int(input("Enter the length of the fish: "))
if fishLength < 42:
    print("Please release the fish back into the lake")
    sizeLimitGap= 42- fishLength
    print("That zander is ", sizeLimitGap,"below the size limit. ")
else:
    print("Zander meets the size limit")

