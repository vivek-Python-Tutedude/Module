"""
we have the following dictionary containing details

user = {
    "user_name" : "my_user"
    "password" : "test@123"
    "email" : "my_user@example.com"
    "address" : "ABC road, 1111"
    "country" : "moon"
        }
        
delete the sensitive info from the dicitionary present in a list 
sensitive_info = ["password", "address"]    
"""

user = {
    "user_name" : "my_user",
    "password" : "test@123",
    "email" : "my_user@example.com",
    "address" : "ABC road, 1111",
    "country" : "moon" 
        }

sensitive_info = ["password", "address","phno"]    

for key in sensitive_info : 
    
    if key in user :
        print(f"Deleted ==> key : {key}, value : {user[key]}")
        user.pop(key)
    else :
        print(f"{key} not persent in  dictionary")
        
print(f"after deleting sensitive data : {user}")

'''

for key in user : 
    if key in sensitive_info :
        user.pop(key)
print(user)

it will gives error because we changing the the length of the dictionary durng using it iside the loop
'''