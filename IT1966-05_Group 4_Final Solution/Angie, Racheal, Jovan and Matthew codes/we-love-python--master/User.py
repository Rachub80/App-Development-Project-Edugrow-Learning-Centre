class User:
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, date_joined, address, level, subject, announcement_descriptions, grade, overall_ratings):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address
        self.__level = level
        self.__subject = subject
        self.__announcement_descriptions = announcement_descriptions
        self.__grade = grade
        self.__overall_ratings = overall_ratings


    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def set_level(self, level):
        self.__level = level

    def set_subject(self, subject):
        self.__subject = subject

    def set_announcement_descriptions(self, announcement_descriptions):
        self.__announcement_descriptions = announcement_descriptions

    def set_grade(self, grade):
        self.__grade = grade

    def set_overall_ratings(self, overall_ratings):
        self.__overall_ratings = overall_ratings


    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address

    def get_level(self):
        return self.__level

    def get_subject(self):
        return self.__subject

    def get_announcement_descriptions(self):
        return self.__announcement_descriptions

    def get_grade(self):
        return self.__grade

    def get_overall_ratings(self):
        return self.__overall_ratings
