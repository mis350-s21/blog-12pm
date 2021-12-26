from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    c = {'post_list': posts,}
    return render(request, 'post_list.html', c)

def pub_post_list(request):
    posts = Post.objects.filter(status=1)
    c = {'post_list': posts,}
    return render(request, 'post_list.html', c)
    
def draft_post_list(request):
    posts = Post.objects.filter(status=0)
    c = {'post_list': posts,}
    return render(request, 'post_list.html', c)

def post_detail(request, id):
    p = Post.objects.get(id=id)
    d = {
        'post': p,
    }
    return render(request, 'post_detail.html', d)


def post_detail_slug(request, s):
    
    # p = Post.objects.get(slug=s)
    p = get_object_or_404(Post, slug=s)
    cs = p.comment_set.all()


    d = {
        'post': p,
        'comments': cs,
    }
    return render(request, 'post_detail.html', d)
    