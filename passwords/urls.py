from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, delete_password

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('delete/<int:password_id>/', delete_password, name='delete_password'),
]
