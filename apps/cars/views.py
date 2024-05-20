from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from .filters import car_filter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer




##########################
#
# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#
######################################

# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         # cars = CarModel.objects.all()
#         # cars = CarModel.objects.filter(Q(brand='Kia') | Q(year=2020) & Q(pk=4))
#         # res = [{'id': car.id, 'brand': car.brand, 'price': car.price, 'year': car.year} for car in cars]
#         # qs = car_filter(self.request.query_params.dict())
#
#         qs = self.get_queryset()
#         # serializer = CarListSerializer(qs, many=True)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         # serializer = CarSerializer(data=data)
#         serializer = self.get_serializer(data=data)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         # CarModel.objects.create(**serializer.data)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         car = self.get_object()
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#
#         # car = get_object_or_404(CarModel, pk=pk)
#         # car_res = {'id': car.id, 'brand': car.brand, 'price': car.price, 'year': car.year}
#         serializer = self.get_serializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         car = self.get_object()
#         #
#         serializer = self.get_serializer(car, data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#
#         # for k, v in data.items():
#         #     setattr(car, k, v)
#
#         # car.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         data = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     # return Response('Not Found', status.HTTP_404_NOT_FOUND)
#         #     raise Http404()
#         car = self.get_object()
#         serializer = self.get_serializer(car, data, partial=True)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     CarModel.objects.get(pk=pk).delete()
#         # except CarModel.DoesNotExist:
#         #     raise Http404()
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
