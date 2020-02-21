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
    category_id = models.ForeignKey( categories, on_delete=models.CASCADE)
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
    category_id = models.ForeignKey( customer, on_delete=models.CASCADE)
    room_id = models.ForeignKey( room, on_delete=models.CASCADE)


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)
    deleted_at = models.TimeField(auto_now_add=True)


class customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)            
    address = models.CharField(max_length=200)            
    phone = models.CharField(max_length=200)            
    email = models.CharField(max_length=200)            
    created_at = models.TimeField(auto_now_add=True)
    deleted_at = models.TimeField(auto_now_add=True)
    country_id = models.ForeignKey( country, on_delete=models.CASCADE)


class amount_booking(models.Model):
    amount = models.IntegerField()