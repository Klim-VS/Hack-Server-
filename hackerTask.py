existing_login = "User133"
existing_password = 1344

reg = input("Register?")
#Yes or No 
reg = reg.strip()
if reg == "Yes":
    print  ("You need to create account") 
    new_log = input ("Your new login?")
    new_log = new_log.strip()
    existing_login = new_log
    
    new_passw = input ("Your new password?")
    new_passw = new_passw.strip()
    existing_password = new_passw
    print ("Now please login")
    
login = input("Your login? ")
login = login.strip()
if login == existing_login :
    print ("Assces granted")
if login  != existing_login:
    print ("Assces Denied")
    
password = input("Your password? ") 
password = password.strip()
if password == existing_password: 
    print ("Assces granted")
if password  != existing_password:
    print ("Assces denided")     
