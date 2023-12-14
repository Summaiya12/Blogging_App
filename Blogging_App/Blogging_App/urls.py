from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Index, name='home'),
    path('about/', views.About, name='about'),
    path('blog/', views.Blog, name='blog'),
    path('', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('post/', views.Post, name='post'),
    path('signouts/', views.signouts, name="signouts"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
