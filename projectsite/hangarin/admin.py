from django.contrib import admin 
from .models import Priority, Note, SubTask, Task, Category

# Register your models here.

admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Note)