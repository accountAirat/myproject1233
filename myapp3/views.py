from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Author, Post


# 1
def hello(request):
    return HttpResponse("Hello World from function!")


# 2
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


# 3
def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


# 4
# http://127.0.0.1:8000/les3/posts/2022/6/
class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


# 5
# http://127.0.0.1:8000/les3/posts/2022/6/python/
def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем,"
                   "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


# 6
def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp3/my_template.html", context)


# 7 if
class TemplIf(TemplateView):
    template_name = "myapp3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context


# 7 for
def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)


# 8
def index(request):
    return render(request, 'myapp3/index.html')


def about(request):
    return render(request, 'myapp3/products.html')


# 9
def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post': post})
