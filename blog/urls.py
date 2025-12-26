from django.urls import path

from blog.views import HomePageListView

urlpatterns = [
   path("", HomePageListView.as_view(), name="index")
]

app_name="blog"