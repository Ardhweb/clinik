from django.urls import path

from. import views

app_name = "account"
urlpatterns = [
    path('register',views.register_new_user,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
]
