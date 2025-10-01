from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
#from django.http import HttpResponse
from .models import Tarefa


# Create your views here.
def home(request):
    lista = Tarefa.objects.all()
    return render(request, "tarefas/home.html", { 'tarefas': lista})


def add(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        form = TarefaForm()

        
    return render(request, "tarefas/adicionar.html", { 'form': form })
    #return HttpResponse("Telinha de adicionar nova tarefa")


def tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, "tarefas/tarefa.html", { 'tarefa': tarefa})

