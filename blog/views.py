from django.shortcuts import render, get_object_or_404
from blog.models import Category

# Create your views here.
def main(request):
    categories = Category.objects.filter(parent__isnull=True)
    context = {
        'categories':categories,
    }
    return render(request, 'blog/main.html', context)

def category(request, category_name):
    category = get_object_or_404(Category, subject=category_name)

    ctgr_tree = [category.subject]
    parent = category.parent
    while parent:
        ctgr_tree.append(parent.subject)
        parent = parent.parent
    ctgr_tree.reverse()

    context = {
        'category':category,
        'categories':category.children.all(),
        'ctgr_tree':ctgr_tree,
        'posts':category.posts.all(),
    }
    
    return render(request, 'blog/category.html', context)