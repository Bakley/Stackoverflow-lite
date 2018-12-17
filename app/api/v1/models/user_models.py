user_data = []


class UserModels():
    """
    Class with CRUD functionalities on the User resource
    """

    def __init__(self):
        self.db = user_data

    def create_user(self, first_name, last_name, username, email, phone, country, password, confirm_password):
        """
        instance method to generate new user into the mock database
        """
        payload = {
            "id": len(self.db) + 1,
            "First Name": first_name,
            "Last Name": last_name,
            "Username": username,
            "Email": email,
            "Phone Number": phone,
            "Country": country,
            "Password": password,
            "Confirm Password": confirm_password
        }
        self.db.append(payload)
        return payload

    def get_all_users(self):
        """
        Retrieve all available user in the database
        """
        return self.db

    def get_one_user(self, id):
        """
        Retrieve on one available user in the database
        """
        single_user = [user for user in self.db if user['id'] == id]
        if single_user:
            return single_user[0]
        else:
            return False

    def get_by_email(self, email):
        """
        Retrieve all available user in the database using email
        """
        single_user = [user for user in self.db if user['Email'] == email]
        if single_user:
            return single_user
        else:
            return False

    def get_by_username(self, username):
        """
        Retrieve all available user in the database using username
        """
        single_user = [
            user for user in self.db if user['Username'] == username]
        if single_user:
            return single_user
        else:
            return False
