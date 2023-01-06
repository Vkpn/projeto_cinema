from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('excluir_filme/<int:id>/', views.excluir_filme, name='excluir_filme'),
    path('mensagem/', views.mensagem, name='mensagem'),
]
