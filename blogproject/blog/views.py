from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify


from .models import Post
from .forms import PostForm

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

def create_post(request):
    f = PostForm(request.POST or None)

    if f.is_valid():
        p = f.save(commit=False)
        p.slug = slugify(p.title)
        p.save()
        return redirect("post_detail_slug", s=p.slug)

    c = {
        'form':f,
    }
    
    return render(request, 'create_post.html', c)
    