from unittest import result
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        users = []
        for user in results:
            print(user)
            users.append(cls(user))
        return users

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        result = connectToMySQL('user_schema').query_db(query, data)
        return result

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('user_schema').query_db(query, data)
        return result