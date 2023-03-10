from django.contrib import admin
from .models import Quiz, Question, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)