from django.views import generic

from blog.models import Post


class HomePageListView(generic.ListView):
    model = Post
    template_name = "main/post_list.html"
    context_object_name = "posts"
    ordering = "-created_time"
