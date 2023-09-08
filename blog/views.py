from django.shortcuts import render
from blog import models
from django.views import generic

# Create your views here.


class BlogView(generic.ListView):
    model = models.PostModel
    template_name = "blog/blog.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return models.PostModel.objects.all()
