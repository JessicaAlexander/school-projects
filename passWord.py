def PassWordCheck(password):
    password_length=len(password)
    lower = 0
    upper = 0
    digits = 0
    special = 0
    space = 1
    flag = 0

    if (password_length>=8):

        for i in range (password_length):

           if ((ord(password[i])>=65 and ord(password[i])<=90)):
               upper=1

           elif (ord(password[i])>=97 and ord(password[i])<=122):
               lower=1

           elif (ord(password[i])>=45 and ord(password[i])<=54):
               digits=1

           elif (password[i]=='~' or password[i]=='!' or password[i]=='@' or password[i]=='*' or password[i]=='^'or password[i]=='%' or password[i]=='$' or password[i]=='&' or password[i]=='#'):
               special=1

           elif (password[i]==' '):
               space=0

        if (lower and upper and digits and special and space):
            print("Password Accepted\n")
            flag=1

        else:
            print("\nPassword did not meet all the requirements. Please try again\n")

    else:
        print("\nPassword did not meet all the requirements. Please try again\n")

    return flag 

print ("PASSWORD REQUIREMENTS\n1: At least 1 uppercase character\n2: At least 1 lowercase character\n3: At least 1 number\n4: At least 1 special character\n5:It cannot contain any spaces, and must be at least 8 characters in length.")
password=input("Enter the password:\n") 
while (password!='Q'): 
    value=PassWordCheck(password) 
    if (value!=1):
        print ("PASSWORD REQUIREMENTS\n1: At least 1 uppercase character\n2: At least 1 lowercase character\n3: At least 1 number\n4: At least 1 special character\n5:It cannot contain any spaces, and must be at least 8 characters in length.")
        password=input("Enter the password:\n")
    else:     
        password='Q' 
