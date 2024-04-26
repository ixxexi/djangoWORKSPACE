class Mydb2Router:
    def db_for_read(model, **hint):
        if model._meta.app_label == "mobilemarket":
            return "mydb2"
        return None

    def db_for_write(model, **hint):
        if model._meta.app_label == "mobilemarket":
            return "mydb2"
        return None

    def allow_relation(obj1, obj2, **hint):
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
