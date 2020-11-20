from django.urls import path
from . import views

urlpatterns = [
    # Wise Welcome
    path('', views.xplanet),
    
    # Redirect for Non-Users
    path('no_user', views.no_user),

    # User Dashboard
    path('dashboard', views.dashboard),

    # Forum Routes
    path('forum', views.forum),
    path('post', views.post),
    path('editpost', views.editpost),
    path('comment', views.comment),
    path('delete', views.delete),

    # Settings
    path('delete', views.delete),
]