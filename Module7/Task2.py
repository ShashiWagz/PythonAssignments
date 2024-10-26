name_list=set()
while True:
    name=input("Enter a name: ")
    if name in name_list:
        print("This Name is Existing name......")

    else:
        print("Please Enter New name...")
        name_list.add(name)

    if name == "":
        break

print("   ")
print("   ")
print("________This is the name_list__________")
for name in name_list:
    print(name)

