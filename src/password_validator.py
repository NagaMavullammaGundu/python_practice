import re, logging

logging.basicConfig(
    filename="passwordValidator_log.log", format="%(asctime)s %(message)s", filemode="w"
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class PasswordValidator:
    """Code will verify that created password is strong or not."""

    def input_password(self):
        """Inputs password from user."""
        self.password = input("Create new password : ")

    def check_length(self):
        """Checks the length of the password."""
        if not len(self.password) >= 8:
            raise ValueError("your password should be atleast 8 characters long")

    def check_upperletters(self):
        """Checks the upper case in the password."""
        if not re.match(r".*[A-Z].*", self.password):
            raise TypeError("your password should contain atleast one upper character")

    def check_lowerletters(self):
        """Checks the lower case in the password."""
        if not re.match(r".*[a-z].*", self.password):
            raise TypeError("your password should contain atleast one lower character")

    def check_numbers(self):
        """Checks numbers are present in password or not."""
        if not re.match(r".*[0-9].*", self.password):
            logger.debug(f"no numbers in password {self.password}")
            raise TypeError("your password should contain atleast one number")

    def validate_password(self):
        """Defines the flow of validating passwords."""
        self.input_password()
        self.check_length()
        self.check_upperletters()
        self.check_lowerletters()
        self.check_numbers()
        logger.info("Your created password met the requirements !!!")


def main():
    logger.info("Password validator")

    pv = PasswordValidator()
    pv.validate_password()


if __name__ == "__main__":
    main()
