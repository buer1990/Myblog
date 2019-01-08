import markdown
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def index(request):
    # return HttpResponse("欢迎访问我的博客网站！")
    # return render(request, "blog/index.html", context={
    #                  'title': '我的博客首页',
    #                  'welcome': '欢迎访问我的博客首页',
    #              })
    post_list = Post.objects.all()
    # print(post)
    return render(request, 'blog/index.html', context={'post_list': post_list, })


def detail(request, pk):
    post0 = get_object_or_404(Post, pk=pk)
    post0.body = markdown.markdown(post0.body, extensions={'markdown.extensions.extra',
                                                           'markdown.extensions.codehilite',
                                                           'markdown.extensions.toc',
                                                           })
    return render(request, 'blog/detail.html', context={'post0': post0})
