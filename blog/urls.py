from django.urls import path


from . import views


app_name = 'blog'

urlpatterns = [
    path('comment/create/', views.create_comment, name='create_comment'),
]
