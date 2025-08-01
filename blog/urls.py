from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index ),
    path('<int:pk>/', views.detail),
    path('create/', views.create, name='blogcreate'),
    path('createfake/', views.createfake),
    path('upload/', views.upload, name='upload_post'),
    path('download/<path:filename>/', views.download, name='download'),
    path('category/<str:slug>/', views.category, name='category'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)