create_password = input("Create new password : ")
upperflag,lowerflag,numberflag = 0,0,0

if len(create_password) >= 8:
    for i in create_password:
        if i >= 'A' and i <= 'Z':
            upperflag = 1
        if i >= 'a' and i <= 'z':
            lowerflag = 1
        if ord(i) >= 48 and ord(i) <= 57:
            numberflag = 1

    if upperflag == 1 and lowerflag == 1 and numberflag == 1:
        print("created password met the requirements")
    if upperflag == 0:
        print("your password missing UPPER letter")
    if lowerflag == 0:
        print("your password missing LOWER letter")
    if numberflag == 0:
        print("your password missing NUMBERS")

else:
    print("Password Length not matched")

    


    