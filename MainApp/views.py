from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet, Comment, LANG_CHOICES
from MainApp.forms import SnippetForm, CommentForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    lang_choice= request.GET.get("lang_choice")
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.filter(public=True)
    if lang_choice == 'all':
        snippets = Snippet.objects.all()
    else:
        snippets = Snippet.objects.filter(lang=lang_choice)
    context['snippets'] = snippets
    context['langs'] = LANG_CHOICES
    context['lang_choice'] = lang_choice
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

@login_required()
def my_snippets(request):
    context = get_base_context(request, 'Мои сниппеты')
    snippets = Snippet.objects.filter(author=request.user)
    context['snippets'] = snippets
    return render(request, 'pages/view_snippets.html', context)

def registration(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            try:
                user = User.objects.create(username=username, email=email, password=password)
            except:
                context = {}
                context['error'] = "Введены некорректные регистрационные данные"
                return render(request, 'pages/index.html', context)

            user.set_password(password)
            user.save()
            new_user = auth.authenticate(request, username=username, password=password)
            auth.login(request, new_user)

            # return redirect('home')

    return redirect('home')

# @login_required()
def comment_add(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.snippet = request.Snippet.id
            comment.save()
            return redirect(f'/snippet_page/{request.Snippet.id}')

    return redirect('home')


def snippet_page(request, id):
    snippet = Snippet.objects.get(id=id)
    comments = Comment.objects.filter(snippet_id=id)
    form_snippet = SnippetForm(instance=snippet)
    form_comment = CommentForm()
    context =get_base_context(request, "Стр сниппета")
    context["form_snippet"] = form_snippet
    context["snippet"] = snippet
    return render(request, 'pages/snippet_page.html', context)