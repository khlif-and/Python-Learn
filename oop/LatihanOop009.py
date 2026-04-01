class User:
    password_used = []
    username_used = []

    def __init__(self, name, email, password, country):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.set_country(country)

        User.password_used.append(password)
        User.username_used.append(name)

    def info(self):
        print(self)

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_country(self):
        return self.__country

    def set_name(self, username_used):
        if username_used in User.username_used:
            raise ValueError("usernama sudah digunakan")

        if len(username_used) < 3:
            raise ValueError("username tidak boleh kurang dari 3 karakter")

        self.__name = username_used
        User.username_used.append(username_used)

    def set_email(self, email):
        allowed = ["@gmail.com", "@yahoo.com", "@outlook.com"]
        if any(domain in email for domain in allowed):
            self.__email = email
        else:
            raise ValueError("email tidak valid")

    def set_password(self, password_used):
        if password_used in User.password_used:
            raise ValueError("password sudah pernah digunakan")

        if len(password_used) < 8:
            raise ValueError("password minimal 8 karakter")

        self.__password = password_used
        User.password_used.append(password_used)

    def set_country(self, country):
        if not country or not country.strip():
            raise ValueError("masukan nama negara")
        self.__country = country

    def __str__(self):
        return f"nama saya adalah {self.__name} email nya adalah {self.__email} passwordnya adalah {self.__password} dan negaranya adalah {self.__country}"


class PremiumUser(User):
    def __init__(self, name, email, password, country, plan):
        super().__init__(name, email, password, country)
        self.__plan = plan

    def get_plan(self):
        return self.__plan

    @staticmethod
    def valid_plan(plan):
        allowed_plans = ["Plus", "Pro", "Family", "Individual"]
        return plan in allowed_plans

    def set_plan(self, plan):
        if PremiumUser.valid_plan(plan):
            self.__plan = plan
        else:
            raise ValueError("plan not exist")

    def __str__(self):
        return f"{super().__str__()} dan plan nya adalah {self.__plan}"


class IndividualUser(PremiumUser):
    def __init__(self, name, email, password, country, plan):
        super().__init__(name, email, password, country, plan)


list_type_user = [
    User("khalif1", "Khalif@gmail.com", "12345678", "Indonesia"),
    PremiumUser("khalif2", "reyna@gmail.com", "khalif223", "Indonesia", "Plus"),
    IndividualUser(
        "khalif3", "reyna@gmail.com", "khalif86161", "Indonesia", "Individual"
    ),
]

for user in list_type_user:
    user.info()
