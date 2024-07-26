from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from polls import views as polls_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', polls_views.index, name='home'),  # Ensure this is correctly handling the root path
]
