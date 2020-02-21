from django.db import models

class role(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=200)
    role_id = models.ForeignKey( role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class password_rest(models.Model):
    pass

class room(models.Model):
    id = models.AutoField(primary_key=True)
    room_numer = models.CharField(max_length=200)
    floor = models.IntegerField()
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    deleted_at = models.TimeField(auto_now_add=True)

class countries(models.Model):
    id = models.AutoField(primary_key=True)
    shortcode = models.CharField(max_length=200)
    title = models.CharField(max_length=40)
    created_at = models.TimeField(auto_now_add=True)
    deleted_at = models.TimeField(auto_now_add=True)

class booking(models.Model):
    id = models.AutoField(primary_key=True)
    time_from = models.DateTimeField(auto_now_add=True, blank=True)
    time_to = models.DateTimeField(auto_now_add=True, blank=True)
    additional_information = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    deleted_at = models.TimeField(auto_now_add=True)

class categories(models.Model):
    pass

class category(models.Model):
    pass

class category_room(models.Model):
    pass

class customer(models.Model)
    pass