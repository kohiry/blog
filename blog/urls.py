from django.urls import path
from blog.views import BlogView

urlpatterns = [path("main/", BlogView.as_view(), name="home")]
