from django.contrib import admin

# Register your models here.
from Evaluation.models import *

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(School_Of)
class School_OfAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Knowledge_areas)
class Knowledge_areasAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(RoleHasPermissions)
class RoleHasPermissionsAdmin(admin.ModelAdmin):
    list

@admin.register(UserHasRole)
class UserHasRoleAdmin(admin.ModelAdmin):
    list


@admin.register(UserHasPermissions)
class UserHasPermissionsAdmin(admin.ModelAdmin):
    list

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('Cycle',)