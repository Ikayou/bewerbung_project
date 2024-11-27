from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('bewerbung_list/', views.bewerbung_list, name='bewerbung_list'),
    path('<int:pk>/', views.bewerbung_detail, name='bewerbung_detail'),
    path('add/', views.BewerbungCreateView.as_view(), name='bewerbung_add'),
    path('<int:pk>/edit/', views.BewerbungUpdateView.as_view(), name='bewerbung_edit'),
    path('<int:pk>/delete/', views.BewerbungDeleteView.as_view(), name='bewerbung_delete'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
