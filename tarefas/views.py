from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "tarefas/home.html")


def add(request):
    return render(request, "tarefas/adicionar.html")
    #return HttpResponse("Telinha de adicionar nova tarefa")


