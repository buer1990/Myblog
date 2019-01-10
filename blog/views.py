import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from blog.models import Post, Category
from comments.forms import CommentForm

"""

"""
# def index(request):
#     # return HttpResponse("欢迎访问我的博客网站！")
#     # return render(request, "blog/index.html", context={
#     #                  'title': '我的博客首页',
#     #                  'welcome': '欢迎访问我的博客首页',
#     #              })
#     post_list = Post.objects.all()
#     # print(post)
#     return render(request, 'blog/index.html', context={'post_list': post_list, })
"""

"""


# IndexView
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 2


# def detail(request, pk):
#     post0 = get_object_or_404(Post, pk=pk)
#     post0.increase_views()
#     post0.body = markdown.markdown(post0.body, extensions={'markdown.extensions.extra',
#                                                            'markdown.extensions.codehilite',
#                                                            'markdown.extensions.toc',
#                                                            })
#
#     # 记得在顶部导入 CommentForm
#     form = CommentForm()
#     # 获取这篇 post 下的全部评论
#     comment_list = post0.comment_set.all()
#     # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据
#     context = {'post0': post0,
#                'form': form,
#                'comment_list': comment_list}
#     return render(request, 'blog/detail.html', context=context)
"""

"""


# PostDetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post0'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()
        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲
        post0 = super(PostDetailView, self).get_object(queryset=None)
        post0.body = markdown.markdown(post0.body, extensions={'markdown.extensions.extra',
                                                               'markdown.extensions.codehilite',
                                                               'markdown.extensions.toc',
                                                               })
        return post0

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list,
        })
        return context


"""

"""


# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month,
#                                     ).order_by('created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

#  ArchivesViews
class ArchivesViews(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('nonth')
        return super(ArchivesViews, self).get_queryset().filter(created_time__year=year,
                                                                created_time__month=month,
                                                                )


"""

"""

# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

"""

"""


# CategoryView
class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


def listing(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': posts})
