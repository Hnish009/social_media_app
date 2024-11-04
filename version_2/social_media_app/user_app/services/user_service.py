from shared.models.user_model import User
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password, full_name='', bio=''):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password, full_name=full_name, bio=bio)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def verify_user(username, password):
        user = UserService.get_user_by_username(username)
        if user and check_password_hash(user.password, password):
            return user
        return None
    
    @staticmethod
    def update_user(username, full_name, bio):
        user = User.query.filter_by(username=username).first()
        if user:
            user.full_name = full_name
            user.bio = bio
            db.session.commit()
            return user
        return None
