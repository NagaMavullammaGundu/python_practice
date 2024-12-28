import re
class PasswordValidator:
    
    def input_password(self):
        self.password = input("Create new password : ")

    def check_length(self):
        if not len(self.password) >= 8:
            raise ValueError("your password should be atleast 8 characters long")

    def check_upperletters(self):   
        if not re.match(r'.*[A-Z].*',self.password):
            raise TypeError("your password should contain atleast one upper character")

    def check_lowerletters(self):
        if not re.match(r'.*[a-z].*',self.password):
            raise TypeError("your password should contain atleast one lower character")

    def check_numbers(self):
        if not re.match(r'.*[0-9].*',self.password):
            raise TypeError("your password should contain atleast one number")

    def validate_password(self):
        self.input_password()
        self.check_length()
        self.check_upperletters()
        self.check_lowerletters()
        self.check_numbers()
        print("Your created password met the requirements !!!")


def main():
    print("Password validator")

    pv = PasswordValidator()
    pv.validate_password()


if __name__ == "__main__":
    main()