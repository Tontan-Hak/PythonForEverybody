#Use  mbox-short.txt as File Name

fname = input("Enter file name: ")

tt = open(fname)
count = 0
for ll in tt:
    if ll.startswith("From "):
        rr = ll.rstrip().split()
        email = rr[1]
        print(email)
        count +=1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")