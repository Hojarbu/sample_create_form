from django.urls import path, include

from main import views

app_name = 'main'
urlpatterns = [
    path('form/', views.UserRequestFormView.as_view(), name='my_form'),
    path('success/', views.success, name='success'),
    path('contact/', views.ContactPageView.as_view(), name='contact_url'),

]
