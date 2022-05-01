from tabnanny import verbose
from django.db import models

# Create your models here.

# 2. Define a model Pizza with a field called name, which will hold name values, such as Hawaiian
#  and Meat Lovers.
# 3. Define a model called Topping with fields called pizza and name. The pizza field should be a
#  foreign key to Pizza, and name should be able to hold values such as pineapple, Canadian
#  bacon, and sausage.
# 4. Register both models with the admin site (Test your work by using the admin site to enter
#  some pizza names and toppings and by using the Django shell to explore the data you
#  entered.)
# 5. Set the username and password for the superuser account to: admin, admin

class Pizza(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        return self.name