class Mydb2Router:
    def db_for_read(self, model, **hint):
        if model._meta.app_label == "mobilemarket":
            return "mydb2"
        return None

    def db_for_write(self, model, **hint):
        if model._meta.app_label == "mobilemarket":
            return "mydb2"
        return None

    def allow_relation(self, obj1, obj2, **hint):
        if (
            obj1._meta.app_label == "mobilemarket"
            or obj2._meta.app_label == "mobilemarket"
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, **hint):
        model_name = hint.pop("model_name", None)
        if app_label == "mobilemarket":
            return db == "mydb2"
        elif db == "mydb2":
            return False
        return None


class Mydb3Router:
    def db_for_read(self, model, **hint):
        if model._meta.app_label == "mysite":
            return "mydb3"
        return None

    def db_for_write(self, model, **hint):
        if model._meta.app_label == "mysite":
            return "mydb3"
        return None

    def allow_relation(self, obj1, obj2, **hint):
        if obj1._meta.app_label == "mysite" or obj2._meta.app_label == "mysite":
            return True
        return None

    def allow_migrate(self, db, app_label, **hint):
        model_name = hint.pop("model_name", None)
        if app_label == "mysite":
            return db == "mydb3"
        elif db == "mydb3":
            return False
        return None
