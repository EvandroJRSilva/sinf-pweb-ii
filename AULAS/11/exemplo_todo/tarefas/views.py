from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa

class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefas/lista_de_tarefas.html'
    context_object_name = 'tarefas'

class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'concluido']
    template_name = 'tarefas/form_tarefa.html'
    success_url = reverse_lazy('lista_de_tarefas')

class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'concluido']
    template_name = 'tarefas/form_tarefa.html'
    success_url = reverse_lazy('lista_de_tarefas')

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'tarefas/tarefa_confirma_excluir.html'
    success_url = reverse_lazy('lista_de_tarefas')