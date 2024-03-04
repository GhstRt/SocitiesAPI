from django.db import models


class Consultant(models.Model):
    name_surname = models.CharField(max_length=60, verbose_name="Consultant Name Surname")
    email = models.CharField(max_length=40, verbose_name="E-Mail")
    position = models.CharField(max_length=100, verbose_name="Position at the University")
    internal_phone_number = models.CharField(max_length=18, verbose_name="Internal Number")


class Activity(models.Model):
    name = models.CharField(max_length=10, verbose_name="Activity Name")


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Club Name")
    prefix = models.CharField(max_length=6, verbose_name="Prefix")
    image_url = models.URLField(verbose_name="Image URL")
    created_date = models.DateField(verbose_name="Created Date")
    members_count = models.IntegerField(verbose_name="Members Count")
    description = models.CharField(max_length=1000, verbose_name="Description")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="activity")
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, related_name="consultant")





