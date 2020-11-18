from django.urls import path
from . import views

urlpatterns = [
    # User Dashboard
    path('', views.xplanet),
    # Forum Routes
    path('forum', views.forum),
    path('post', views.post),
    path('comment', views.comment),
    path('delete', views.delete),
]