from django.contrib import admin
from django.urls import path
from post.views import index,category,tags,PostDetails, Contact, ContactSuccess
from django.views.generic import TemplateView



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('categories/<slug:category_slug>', category,name='categories'),
    path('tags/<slug:tag_slug>', tags, name='tags'),
    path('<slug:post_slug>', PostDetails, name='articleDetails'),
    path('contact/', Contact, name='contact'),
    path('contact/success/', ContactSuccess, name='contactsuccess'),
]
