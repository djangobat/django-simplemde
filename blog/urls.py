from django.urls import path


from . import views


app_name = 'blog'

urlpatterns = [
    path('comment/create/', views.create_comment, name='create_comment'),
    path('ajax/image/upload/', views.ajax_image_upload, name='ajax_image_upload'),
    path('ajax/image/<int:image_id>/width/change/', views.ajax_change_width, name='ajax_change_width'),
    path('ajax/image/<int:image_id>/delete/', views.ajax_delete_image, name='ajax_delete_image'),
]
