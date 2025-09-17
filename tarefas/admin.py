from django.contrib import admin
from .models import Tarefa

# Register your models here.

class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'criada_em']


admin.site.register(Tarefa, TarefaAdmin)