from django.urls import path
from .views import HomePageView, AbouutPageView, EmployeesPageView
# from django.contrib import admin

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AbouutPageView.as_view(), name='about'),
    path('employees/', EmployeesPageView.as_view(), name='employees'),
    # path('admin/', admin.site.urls, name='admin')
]
