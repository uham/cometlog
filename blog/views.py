from django.shortcuts import render

# Create your views here.
def main(request):
    context = {}
    return render(request, 'blog/main.html', context)