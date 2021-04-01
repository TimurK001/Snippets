from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)

@login_required()
def add_snippet_page(request):
    # request.user
    if request.method=="GET":
        form = SnippetForm()
        context = get_base_context(request, 'Добавление нового сниппета')
        context['form'] = form
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect('snippets_list')
    # return redirect('home')


def snippets_page(request):
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.all()
    context['snippets'] = snippets
    return render(request, 'pages/view_snippets.html', context)

def snippets_edit(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
    except Snippet.DoesNotExist():
        raise Http404

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            context = {}
            context['error'] = "Неверный логин или пароль"
            return  render(request, 'pages/index.html', context)
    return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')


