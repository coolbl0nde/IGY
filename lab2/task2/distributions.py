from typing import Set
import re
import json

class MySet(Set):
    def __init__(self, list_elements=()):
        super().__init__(list_elements)

    def grep(self, regex):
        elements = []

        for element in self:
            if re.findall(regex, element):
                elements.append(element)

        return elements

    def list(self):
        elements = []

        for element in self:
            elements.append(element)

        return elements

    def find(self, value):
        for element in self:
            if element == value:
                return True

        return False

class MyDataBase():
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        self.users[username] = MySet()

    def user_exist(self, username):
        for user in self.users.keys():
            if username == user:
                return True

        return False

    def add_element(self, username, element):
        self.users[username].add(element)

    def remove_element(self, username, element):
        self.users[username].remove(element)

    def find_element(self, username, element):
        return self.users[username].find(element)

    def grep_element(self, username, element):
        return self.users[username].grep(element)

    def list_element(self, username):
        return self.users[username].list()

    def save_data(self):
        final_users = {}

        for user in self.users.keys():
            final_users[user] = self.list_element(user)

        with open("storage.json", "w") as file:
            json.dump(final_users, file)

    def load_data(self, user):

        with open("storage.json", "r") as file:
            final_users = json.load(file)

        if user in final_users:
            self.users[user] = MySet(final_users[user] + self.list_element(user))
            return True

        else:
            return False

