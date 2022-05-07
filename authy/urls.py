from django.urls import path
from authy.views import Profile, Login, Signup

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('profile/',Profile,name='profile'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('signup/',Signup,name='signup'),
  
]