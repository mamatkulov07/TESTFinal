from django.urls import path
from .views import *

urlpatterns = [
    path('userprofile/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('food/', FoodViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='food_list'),
    path('food/<int:pk>/', FoodViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='food_detail'),

    path('courier/', CourierViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='courier_list'),
    path('courier/<int:pk>/', CourierViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='courier_detail'),

    path('order/', OrderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='order_list'),
    path('order/<int:pk>/', OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),

    path('delivery/', DeliveryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='delivery_list'),
    path('delivery/<int:pk>/', DeliveryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='delivery_detail'),

    path('rating/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='rating_list'),
    path('rating/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),

    path('review/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
    path('review/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),

]