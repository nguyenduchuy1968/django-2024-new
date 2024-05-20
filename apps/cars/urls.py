from django.urls import path
# from cars.views import CarTestView, CarDetailView
from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView


urlpatterns = [
    path('', CarListCreateView.as_view(), name= 'car_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_delete')
]