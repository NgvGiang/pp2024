class Course:
    def __init__(self, id, name, num_credits):
        self.__id = id
        self.__name = name
        self.__num_credits = num_credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_num_credits(self):
        return self.__num_credits

    def display(self):
        print("Course: ", self.__name, "\nID: ", self.__id)