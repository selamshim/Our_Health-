from . import views
from django.urls import path

urlpatterns = [
    path('', views.IssueList.as_view(template_name="post/post_list.html"), name='home'),
]