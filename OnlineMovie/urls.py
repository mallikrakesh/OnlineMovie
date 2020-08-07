"""OnlineMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from App1 import views
from OnlineMovie import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    #Admin Operation
    path('admin_login/',views.movieAdminLogin,name='admin_login'),
    path('admin_login_page/',views.movieAdminLoginPage,name='admin_login_page'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('save_movie/',views.save_movie,name='save_movie'),
    path('view_movie/',views.view_movie,name='view_movie'),
    path('delete_movie/',views.delete_movie,name='delete_movie'),

#Customer Operation

    path('customer_page', views.showIndex, name='main'),
    path('login_page',views.loginPage,name='login_page'),
    path('create_customer_account/',views.create_customer_account,name='create_customer_account'),
    path('save_customer/',views.save_customer,name='save_customer'),
    path('login_customer/',views.login_customer,name='login_customer'),
    path('searchaction/',views.searchaction,name='searchaction'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
