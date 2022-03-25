def check_pasword(psw):
    import re # import regular expression module
    if len(psw) < 8:
        raise Exception("Password must be at least 8 characters long")
    elif not re.search("[a-z]", psw):
        raise Exception("Password must contain at least one lowercase letter")
    elif not re.search("[A-Z]", psw):
        raise Exception("Password must contain at least one uppercase letter")
    elif not re.search("[0-9]", psw):
        raise Exception("Password must contain at least one digit")
    elif not re.search("[$#@]", psw):
        raise Exception("Password must contain at least one special character")
    elif re.search("\s", psw):
        raise Exception("Password must not contain spaces")
    else:
        print("Password is valid")        

pasword = input("Enter password: ") 
try: 
    check_pasword(pasword) 
except Exception as e:
    print(e)