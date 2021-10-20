from django.urls import path
from quickstart import views


urlpatterns = [
    path('', views.ListBookAPIView.as_view(), name='book_list'),
    path('create/', views.CreateBookAPIView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.UpdateBookAPIView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.DeleteAPIView.as_view(), name='book_delete')
]