from django.contrib import admin
from .models import Creator,Language, Frameworks, Programmer

# Register your models here.
admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Frameworks)
admin.site.register(Programmer)
