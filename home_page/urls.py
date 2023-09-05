
from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.home, name = 'home'),
    path('detail/<int:hotel_id>/', views.hotel_detail, name = 'hotel_detail'),
    path('review/<int:hotel_id>/', views.review, name = 'review_hotel'),
    path('edit/<int:review_id>/', views.edit_review, name = 'edit'),
    path('search/', views.search_hotel, name = 'search'),
    path('delete<int:review_id>/', views.delete, name = 'delete')
    
]