from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method=="GET":
        form = SnippetForm()
        context = get_base_context(request, 'Добавление нового сниппета')
        context['form'] = form
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('snippets_list')


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

