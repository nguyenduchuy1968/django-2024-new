from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    # pagination_class = PagePagination
    queryset = CarModel.objects.all()
    filterset_class = CarFilter

    # def get_queryset(self):
    #     # filter
    #     return car_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         print(car.auto_park)
#         return Response('ok')
