from django.urls import path
from . import views

urlpatterns = [
    # Wise Welcome
    path('', views.xplanet),

    # User Dashboard
    path('dashboard', views.dashboard),

    # Forum Routes
    path('forum', views.forum),
    path('post', views.post),
    path('comment', views.comment),
    path('delete', views.delete),
]