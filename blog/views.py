from django.shortcuts import render
from django.views import generic

from blog import models

# Create your views here.
if 1 == None:
    pass


class BlogView(generic.ListView):
    model = models.PostModel
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return models.PostModel.objects.all()
