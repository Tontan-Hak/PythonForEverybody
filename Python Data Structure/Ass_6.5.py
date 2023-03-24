# Assignmnet 6.5
text = "X-DSPAM-Confidence:    0.8475";
text =text.replace("","")
ind=text.find(":")
print(float(text[ind+1:]))
# other way
text = "X-DSPAM-Confidence:    0.8475";

spacePos = text.find(" ")
number = text[spacePos::1]
#not really necessary but since we are just learning and playing
strippedNumber = number.lstrip();
result = float(strippedNumber)

def reprint(printed):
    print(printed) 

reprint(result)