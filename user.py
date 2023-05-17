class User:
    """A class to model a typical User."""
    def __init__(self, first_name, last_name, profile_pic, username, city):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_pic = profile_pic
        self.username = username
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        user_info = {}
        user_info['first name'] = self.first_name
        user_info['last name'] = self.last_name
        user_info['profile pic'] = self.profile_pic
        user_info['username'] = self.username
        user_info['city'] = self.city
        user_info['login attempts'] = self.login_attempts

        return user_info

    def greet_user(self):
        print(f"Good evening {self.username}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts_count(self):
        print(self.login_attempts)

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can be user"]

    def show_privileges(self):
        print(f"privileges: ")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, profile_pic, username, city):
        super().__init__(first_name, last_name, profile_pic, username, city)
        self.privileges = Privileges()

    # def show_privileges(self):
    #     print(f"{self.username} privileges:")
    #     for privilege in self.privileges:
    #         print(f"\t- {privilege}")


harold = User("harold", "hightop", "harold_funny.jpeg", "HealthyHarold01", "Sydney")
mercy = User("meira", "knock", "show_mercy.jpeg", "No_Mercy", "new york city")
canly = User("newton", "canly", "random.png", "CanlyCan", "Ottawa")

# print(harold.describe_user())
# print(mercy.describe_user())
# print(canly.describe_user())

# # harold.greet_user()
# # mercy.greet_user()
# # canly.greet_user()

# # harold.increment_login_attempts()
# # harold.increment_login_attempts()

# # harold.show_login_attempts_count()

# # harold.reset_login_attempts()
# # harold.show_login_attempts_count()


niles = Admin("niles", "crane", "eddie.jpeg", "seattlesPremierePsych", "Seattle")
niles.privileges.show_privileges()