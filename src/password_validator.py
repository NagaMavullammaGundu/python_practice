class PasswordValidator:
    def __init__(self):
        print("password validator object is craeted")

    def input_password(self):
        self.password = input("Create new password : ")

    def check_length(self):
        if not len(self.password) >= 8:
            raise ValueError("your password should be atleast 8 characters long")

    def check_upperletters(self):
        upperflag = True
        for i in self.password:
            if "A" <= i <= "Z":
                upperflag = False
                break
        if upperflag:
            raise TypeError("your password should contain atleast one upper character")

    def check_lowerletters(self):
        lowerflag = True
        for j in self.password:
            if "a" <= j <= "z":
                lowerflag = False
                break

        if lowerflag:
            raise TypeError("your password should contain atleast one lower character")

    def check_numbers(self):
        numberflag = True
        for i in self.password:
            if ord(i) >= 48 and ord(i) <= 57:
                numberflag = False
        if numberflag:
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
