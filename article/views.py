from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Article, Comment
from .forms import ArticleForm
from django.core.paginator import Paginator

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "articles.html", {"page_obj":page_obj})

def index(request):
    context = {
        "number1":20
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html", context)

@login_required
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarılı bir şekilde eklendi")
        return redirect("article:dashboard")
    return render(request, "addarticle.html", {"form":form})

@login_required
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(request, "detail.html", {"article": article, "comments":comments})

@login_required
def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if article.author == request.user:
        if form.is_valid():
            article = form.save(commit = False)
            article.author = request.user
            article.save()
            messages.success(request, "Makale başarılı bir şekilde güncellendi")
            return redirect("article:dashboard")
    else:
        messages.info(request, "Makale size ait değil...")
        return redirect("article:dashboard")
    return render(request, "update.html", {"form":form})

@login_required
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if article.author == request.user:
        article.delete()
        messages.success(request, "Makale başarı ile silindi...")
        return redirect("article:dashboard")
    else: 
        messages.info(request, "Makale size ait değil...")
        return redirect("article:dashboard")


def add_comment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        comment = Comment(comment_author=comment_author, comment_content=comment_content)
        comment.article = article
        comment.save()
        messages.success(request, "Yorum Eklendi")
    return redirect(reverse("article:detail",kwargs={"id":id}))
    