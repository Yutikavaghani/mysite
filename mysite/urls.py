"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from myapp.views import indexpage
from myapp.views import contactpage
from myapp.views import aboutpage
from myapp.views import bloggridpage
from myapp.views import blogsinglepage
from myapp.views import blogpage
from myapp.views import clientspage
from myapp.views import index2page
from myapp.views import popoverpage
from myapp.views import servicespage
from myapp.views import singleproject
from myapp.views import tweenlite
from myapp.views import columnthree
from myapp.views import columnfour

from myadminapp.views import adminindex
from myadminapp.views import registerdata
from myadminapp.views import adminlogin
from myadminapp.views import viewdata
from myadminapp.views import deletedata
from myadminapp.views import edit_data
from myadminapp.views import slideradddata
from myadminapp.views import slider
from myadminapp.views import slider_delete
from myadminapp.views import slider_edit
from myadminapp.views import offer_add
from myadminapp.views import offer_view  
from myadminapp.views import offer_edit  
from myadminapp.views import offer_delete  
from myadminapp.views import category_add  
from myadminapp.views import category_view  
from myadminapp.views import cat_delete  
from myadminapp.views import cat_edit  
from myadminapp.views import blog_add , blog_view , blog_delete , blog_edit





urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexpage),
    path('contact/', contactpage),
    path('about/', aboutpage),
    path('bloggrid/', bloggridpage),
    path('blogsingle/<int:pk>/', blogsinglepage, name='blogsingle'),
    path('blog/', blogpage),
    path('clients/', clientspage),
    path('index-2/', index2page),
    path('popover/', popoverpage),
    path('services/', servicespage),
    path('singleproject/', singleproject),
    path('tweenlite/', tweenlite),
    path('columnthree/', columnthree),
    path('columnfour/', columnfour),


    path('adminindex/', adminindex),
    path('admin-register/', registerdata),
    path('admin-login/', adminlogin),
    path('admin-viewdata/', viewdata),
    path('delete-data/<str:pk>/',deletedata),
    path('edit-data/<int:pk>/', edit_data),

    path('slider-adddata/', slideradddata),
    path('slider-viewdata/', slider),
    path('slider-delete/<str:pk>/', slider_delete),
    path('slider-edit/<int:pk>/', slider_edit),

    path('offer-add/', offer_add),
    path('offer-view/', offer_view),
    path('offer-delete/<str:pk>/', offer_delete),
    path('offer-edit/<int:pk>/', offer_edit),

    path('category-add/', category_add),
    path('category-view/', category_view),
    path('category-delete/<str:pk>/', cat_delete),
    path('category-edit/<int:pk>/', cat_edit),

    path('blog-add/', blog_add),
    path('blog-view/', blog_view),
    path('blog-delete/<str:pk>/', blog_delete),
    path('blog-edit/<int:pk>/', blog_edit),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)