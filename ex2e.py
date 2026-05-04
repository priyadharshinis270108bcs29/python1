password=input("enter your password")
has_digit=False
has_lower=False
has_upper=False
has_special=False
has_space=False
if len(password)>15:
    print("password invalid")
else:
    for ch in password:
        if ch.isdigit():
            has_digit=True
        elif ch.isupper():
            has_upper=True
        elif ch.islower():
            has_lower=True
        elif ch.isspace():
            has_space=True
        else:
            has_special=True
if has_space:
    print("invalid password")
elif has_digit and has_lower and has_upper and has_special:
    print("password is valid")
else:
    print("your password is invalid")
    print("the password does not fall under the given conditions")


