from helpers import helpers

password_length = helpers.enter_password_length()

if not helpers.verify_password_length(password_length):
    raise Exception("Le script va prendre fin, la longeur minimal est de 12")

print(helpers.generate_password(password_length))

    
    
    

