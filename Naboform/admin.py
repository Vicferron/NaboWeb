from django.contrib import admin
from Naboform.models import Infonabo

# Register your models here.
class InfonaboAdmin(admin.ModelAdmin):
    list_display=("usuario", "precio", "time")

admin.site.register(Infonabo, InfonaboAdmin)