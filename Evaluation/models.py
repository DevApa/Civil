from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} creada correctamente..!"
        return self.name

class School_Of(models.Model):
    University = models.ForeignKey(University, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} creada correctamente"
        return self.name

class Career(models.Model):
    School_Of = models.ForeignKey(School_Of, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Cycle(models.Model):
    name = models.CharField(max_length=100)
    cycle_active = models.CharField(max_length=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Knowledge_areas(models.Model):
    name = models.CharField(max_length=255)
    University = models.ForeignKey(University, null=False, blank=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Matter(models.Model):
    name = models.CharField(max_length=255)
    Career = models.ForeignKey(Career, null=False, blank=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    second_last_name = models.CharField(max_length=60)
    identify = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    profile_path_img = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    Career = models.ForeignKey(Career, null=False, blank=False, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    name = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Permission(models.Model):
    name = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class RoleHasPermissions(models.Model):
    Role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.CASCADE)
    Permission = models.ForeignKey(Permission, null=False, blank=False, on_delete=models.CASCADE)

class UserHasRole(models.Model):
    User = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, null=False, blank=False, on_delete=models.CASCADE)

class UserHasPermissions(models.Model):
    User = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    Permission = models.ForeignKey(Permission, null=False, blank=False, on_delete=models.CASCADE)

class Answer(models.Model):
    result = models.PositiveSmallIntegerField()
    User = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    Question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.CASCADE)
    Cycle = models.CharField(max_length=20)
    Category = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    Knowledge_areas = models.CharField(max_length=30)
    Observation = models.CharField(max_length=255, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
