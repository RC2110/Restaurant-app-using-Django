from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE=(
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_course", "Main Course"),
    ("deserts", "Deserts")
     )

AVAIL =(
    (0, "Unavailable"),
    (1,"Available")
)

class MenuApp(models.Model):
    menu = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    meal_type = models.CharField(max_length=1000, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT) # models.CASCADE or models.NULL can also be used.
    status = models.CharField(max_length=1000, choices=AVAIL, default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu
