text=input("enter a pattern")
result=""
i=0
while i<len(text):
    letter=text[i]
    number=int(text[i+1])
    result +=letter*number
    i+=2
    print(result)


