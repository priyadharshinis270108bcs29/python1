s=input("enter a string")
vowels="aeiouAEIOU"
v_count=0
c_count=0
for c in s:
    if c in vowels:
        v_count+=1
    else:
        c_count+=1
print("the vowels",v_count)
print("the consonant",c_count)
