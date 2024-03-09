class users:
    def __init__(self,user_id, email, password_hash, salt, user_type_id, is_active):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.salt = salt
        self.user_type_id = user_type_id
        self.is_active = is_active