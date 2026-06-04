#Password_Strength_Checker
print("***Password Analyser.***")
password = input("Enter your password here: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for i in password:
    if i.isupper():
        has_upper = True
    elif i.islower():
        has_lower = True
    elif i.isdigit():
        has_digit = True
    else:
        has_special = True

print("------------------")
print(f"Length: {'✔️' if len(password)>=8 else '❌'} ")
print(f"Uppercase: {'✔️' if has_upper else '❌'} ")
print(f"Lowercase: {'✔️' if has_lower else '❌'} ")
print(f"Digit: {'✔️' if has_digit else '❌'} ")
print(f"Special Character: {'✔️' if has_special else '❌'} ")

if ( len(password)>=8 and has_upper and has_lower and has_digit and has_special ):
    print("Strong password.")
else:
    print("Weak password.")