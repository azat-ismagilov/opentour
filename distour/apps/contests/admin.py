from django.contrib import admin

# Register your models here.
from .models import Contest, Problem,Participation

admin.site.register(Contest)
admin.site.register(Problem)
admin.site.register(Participation)
