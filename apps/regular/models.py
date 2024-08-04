from django.db import models

class Task(models.Model):
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Standard(models.Model):
    comment = models.CharField(max_length=200)
    template = models.CharField(max_length=100)
    zoom = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Guestalk(models.Model):
    day = models.CharField(max_length=5)
    vol = models.CharField(max_length=2)
    guest = models.CharField(max_length=100)
    guest_url = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    template = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    spreadsheet = models.CharField(max_length=100)
    zoom = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title