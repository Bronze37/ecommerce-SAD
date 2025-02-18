# filepath: /D:/Software_Architecture/nddong_project1/nddong_project1/dbrouters.py
class BookRouter:
    """
    A router to control all database operations on models in the
    book application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read book models go to mongodb.
        """
        if model._meta.app_label == 'book':
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write book models go to mongodb.
        """
        if model._meta.app_label == 'book':
            return 'mongodb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the book app is involved.
        """
        if obj1._meta.app_label == 'book' or \
           obj2._meta.app_label == 'book':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the book app only appears in the 'mongodb'
        database.
        """
        if app_label == 'book':
            return db == 'mongodb'
        return None