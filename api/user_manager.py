import random
from .config import session
from .models.user import User

class UserManager:
    @classmethod
    def insert(cls, user: User):
        session.add(user)
        session.commit()

    @classmethod
    def delete(cls, user: User):
        session.query(User). \
                filter(User.viewer_id == user.viewer_id and User.user_id == user.user_id). \
                delete()
        session.commit()

    @classmethod
    def get_user_by_viewer_id(cls, id: int) -> User:
        user = session.query(User). \
                       filter(User.viewer_id == id). \
                       first()

        return user

    @classmethod
    def get_user_by_user_id(cls, id: int) -> User:
        user = session.query(User). \
                       filter(User.user_id == id). \
                       first()

        return user

    @classmethod
    def has_viewer_id(cls, id: int) -> bool:
        for user in cls.get_all():
            if user.viewer_id == id:
                return True
        return False

    @classmethod
    def has_user_id(cls, id: int) -> bool:
        for user in cls.get_all():
            if user.user_id == id:
                return True
        return False

    @classmethod
    def update_viewer_id(cls, old_id: int, new_id: int):
        user = cls.get_user_by_viewer_id(old_id)
        user.viewer_id = new_id
        session.commit()

    @classmethod
    def update_user_id(cls, old_id: int, new_id: int):
        user = cls.get_user_by_user_id(old_id)
        user.user_id = new_id
        session.commit()

    @classmethod
    def get_all(cls) -> list:
        return session.query(User).all()

    @classmethod
    def generate(cls, name: str) -> User:
        while True:
            viewer_id, user_id = random.randint(100000000, 999999999), random.randint(100000000, 999999999)
            if not (cls.has_viewer_id(viewer_id) or cls.has_user_id(user_id)):
                user = User(viewer_id, user_id, name)
                cls.insert(user)

                return user
