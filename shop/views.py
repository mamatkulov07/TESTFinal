from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .serialazers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class FoodViewSets(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'resto_name', 'price']
    search_fields = ['resto_name']


class CourierViewSets(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializers


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class DeliveryViewSets(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializers


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

