from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=200, unique=True)
    hashed_password = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username
