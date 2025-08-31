"""
URL configuration for art project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from art import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your url patterns
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name="index" ), 
    path('home/',views.home, name="home"), 
    path('artworks/',views.artworks, name="all_artworks"),
    path('cart/',views.cart, name="cart"),
    path('learn/',views.learn, name="learn_art"),
    path('contact/',views.contact, name="contact"),
     path('header/',views.header,name='header'),
      path('purchase/',views.purchase,name="purchase"),
       path('profile/',views.profile,name="profile"), 
      path('',views.login_signup,name="login_signup"),
        path('logout/',views.logout_page,name='logout_page'),
]