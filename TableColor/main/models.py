from django.db import models


class Table(models.Model):
    usersL = [{
        "name": "Armen",
        "age": 25
    },
     {
        "name": "Anna",
        "age": 23
    },
    ]

    def __str__(self):
        return self.usersL

