from django.contrib import admin 
from .models import Priority, Note, SubTask, Task, Category

# Register your models here.
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category")
    list_filter = ("status", "priority", "category",)
    search_fields = ("title", "description",) 

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "get_parent_task")
    list_filter = ("status",)
    search_fields = ("title",) 

    def get_parent_task(self, obj):
        try:
            parent_task = Task. objects.get(id=obj.id)
            return parent_task.title
        except Task.DoesNotExist:
            return None
        
    get_parent_task.short_description = "Parent Task"

@admin.register(Note)  
class NoteAdmin(admin.ModelAdmin):  
     list_display = ("task", "content", "created_at",)
     list_filter = ("created_at",)
     search_fields = ("content",) 