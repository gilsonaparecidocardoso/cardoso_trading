from django.contrib import admin

# Register your models here.
from coins import models

@admin.register(models.MoedasADM)
class MoedasAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'email'