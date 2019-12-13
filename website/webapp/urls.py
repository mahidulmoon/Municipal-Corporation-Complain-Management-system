from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('detail/',views.details,name="detail"),
    path('information/',views.information,name="information"),
    path('login/',views.login,name="login"),
    path('registration/',views.register,name='registration'),
    path('logout/',views.logout,name='logout'),
    path('forgetpassword/',views.fpass,name='change-password'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('complain/',views.complain,name='complain')
]
