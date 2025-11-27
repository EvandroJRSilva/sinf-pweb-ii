from django.urls import path
from .views import TarefaListView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView

urlpatterns = [
    path('', TarefaListView.as_view(), name='lista_de_tarefas'),
    path('criar/', TarefaCreateView.as_view(), name='criar_tarefa'),
    path('<int:pk>/atualizar/', TarefaUpdateView.as_view(), name='atualizar_tarefa'),
    path('<int:pk>/excluir/', TarefaDeleteView.as_view(), name='excluir_tarefa')
]