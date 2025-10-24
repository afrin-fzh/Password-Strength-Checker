import string
print("Welcome To The Password Strength Checker :)")
while 1:
    choice = input("Do you want to check your password's strength (y/n): ")
    if choice=='y':
        password=input("Enter the password: ")
        lower_case_count = upper_case_count = number_count = whitespace_count = special_count = 0
        for c in list(password):
            if c in string.ascii_lowercase:
                lower_case_count += 1
            elif c in string.ascii_uppercase:
                upper_case_count += 1
            elif c in string.digits:
                number_count += 1
            elif c == ' ':
                whitespace_count += 1
            else:
                special_count += 1
        strength = 0
        

        if lower_case_count >= 1:
            strength += 1
        if upper_case_count >= 1:
            strength += 1
        if number_count >= 1:
            strength += 1
        if whitespace_count >= 1:
            strength += 1
        if special_count >= 1:
            strength += 1

        if strength == 1:
            remarks = "Password is not secure. Easy to guess!"
        elif strength == 2:
            remarks = "Password is easy. Make it tougher!"
        elif strength == 3:
            remarks = "Password is ok. Should be more secure"
        elif strength == 4:
            remarks = "Very good password! Can be made more secure"
        elif strength == 5:
            remarks = "Very STRONG password!"

        print("Your password has:")
        print(lower_case_count, "lowercase letters")
        print(upper_case_count, "uppercase letters")
        print(number_count, "digits")
        print(whitespace_count, "whitespaces")
        print(special_count, "special characters")
        print("Password score:", strength)
        print("Remarks:", remarks)
    elif choice=='n':
        print('Thank you!')
        
 
    else:
        print('Please type y or n.')
    print()

    

    


