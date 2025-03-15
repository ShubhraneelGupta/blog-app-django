from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>', views.post_details, name='post_details'),
    path('<int:post_id>/share', views.post_share, name='post_share'),
    path('<int:post_id>/comment', views.post_comment, name='post_comment'),
    path('search/', views.post_search, name='post_search')
]