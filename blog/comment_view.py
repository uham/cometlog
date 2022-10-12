from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Comment, Post

@login_required(login_url='account:signin')
def comment_add(request):
    if request.method == 'POST':
        try:
            comment = Comment()
            comment.content = request.POST['comment-content']
            comment.writer = request.user
            comment.post = Post.objects.get(slug=request.POST['slug'])
        except:
            return redirect('blog:main')

        try:
            comment.full_clean()
            comment.save()
        except:
            pass

        return redirect('blog:post_detail', request.POST['slug'])
    else:
        return redirect('blog:main')