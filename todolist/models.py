from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)

    @classmethod
    def get_all_todo(cls):
        return cls.objects.all()
    
    @classmethod
    def create_todo(cls, title):
        new_todo = cls(title=title)
        new_todo.save()

    @classmethod
    def delete_todo(cls, todo_id):
        todo = cls.objects.get(id=todo_id)
        todo.delete()
         
    def __str__(self):
        return self.title