from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all() #llevo los valores de todos los objectos a posts
    return render(request,"blog/blog.html",{'posts':posts}) #Retorno una lista con todos los valores como un query set

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})#Retornamos una nueva vista con el filtro de categoria

    
