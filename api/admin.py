from django.contrib import admin
from .models import Module
from .models import Professor
from .models import ProfRating

admin.site.register(Module)
admin.site.register(Professor)
admin.site.register(ProfRating)

# Register your models here.
