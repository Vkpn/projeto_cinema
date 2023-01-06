from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Filme, Horarios
from django.core.mail import send_mail


def home(request):
    if request.method == 'GET':
        filmes = Filme.objects.all()
        horarios = Horarios.objects.all()
        return render(request, 'home.html', {'filmes': filmes, 'horarios': horarios})

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        lancamento = request.POST.get('lancamento')
        diretor = request.POST.get('diretor')
        genero = request.POST.get('genero')
        capa = request.FILES.get('capa_do_filme')
        idioma = request.POST.get('idioma')
        lista_horario = request.POST.getlist('hora')
        sala = request.POST.get('sala')
        sinopse = request.POST.get('sinopse')

        if not capa:
            messages.error(request, 'Selecionar uma capa para o filme.')
            return render(request, 'cadastro.html', {'nome': nome, 'lancamento': lancamento, 'diretor': diretor, 'genero': genero, 'idioma': idioma, 'sala': sala, 'sinopse': sinopse})

        if len(lista_horario) == 0:
            messages.error(request, 'Preencher ao menos um horario de exibição.')
            return render(request, 'cadastro.html', {'nome': nome, 'lancamento': lancamento, 'diretor': diretor, 'genero': genero, 'idioma': idioma, 'sala': sala, 'sinopse': sinopse})
        else:
            filme = Filme(
            nome = nome,
            lancamento = lancamento,
            diretor = diretor,
            genero = genero,
            capa = capa,
            idioma = idioma,
            sala = sala,
            sinopse = sinopse
        )

            filme.save()
            filme.horarios_filmes.add(*lista_horario)
            filme.save()
            messages.success(request, 'Filme cadastrado com sucesso!')
            return redirect('/cadastro')
            

def listar(request):
    if request.method == 'GET':
        filmes = Filme.objects.all()
        horarios = Horarios.objects.all()
        return render(request, 'listar.html', {'filmes': filmes, 'horarios': horarios})

def excluir_filme(request, id):
    filme = Filme.objects.get(id=id)
    filme.delete()
    messages.success(request, 'Filme excluido com sucesso!')
    return redirect('listar')

def mensagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_contato')
        endereco = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        send_mail(f'{nome}', f'{endereco} \n\n {mensagem}', f'teste.vkpn@gmail.com', ['thayzepcd@gmail.com'])
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('home')
