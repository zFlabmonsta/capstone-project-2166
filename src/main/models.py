from django.db import models

# Create your models here.
class Dashboard(models.Model):
    """
    Each user that signs up will be assigned their on Dashboard
    to hold and save their classes, where each class will 
    save the lecturer's evaluated learning outcome 
    """
    dashboard_name = models.CharField(max_length=200)

class MyClass(models.Model):
    """
    MyClass is created by the lecturer and stores learning outcomes
    that are evaluated and wanted.
    """
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=20)

class Learning_outcome(models.Model):
    """
    contains learning outcomes
    """
    my_class = models.ForeignKey(MyClass, on_delete=models.CASCADE)
    learning_outcome = models.CharField(max_length=1000)

