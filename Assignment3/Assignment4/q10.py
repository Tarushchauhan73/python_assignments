class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password 

    def verify_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Old password is incorrect.")


user = UserAccount("Tarush", "12345")


print("Password correct:", user.verify_password("12345"))


user.change_password("12345", "67890")


print("New password correct:", user.verify_password("67890"))