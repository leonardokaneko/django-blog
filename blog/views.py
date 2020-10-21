from django.shortcuts import render
from .models import Posts, User
from django.views.generic import ListView


def index(request):
    posts = Posts.objects.order_by('-created_at')
    return render(request, 'layout.html', {'posts': posts})


def post(request, post_id):
    post = Posts.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})


class SearchResultsView(ListView):
    model = Posts
    template_name = 'busca.html'

    def get_queryset(self):
        self.query = self.request.GET.get('q')
        qset = Posts.objects.order_by('-created_at')
        object_list = qset.filter(title__icontains=self.query)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = self.query
        return context


def author_find(request):
    author_id = request.GET.get('author')
    user = User.objects.get(pk=author_id)
    posts = Posts.objects.order_by('-created_at').filter(author__pk=author_id)
    return render(request, 'autor.html', {'posts': posts, 'user': user})
