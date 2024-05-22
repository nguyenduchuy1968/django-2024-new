
from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    brand = filters.CharFilter('brand', 'icontains')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'price'
        )
    )




# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.exceptions import ValidationError
#
# from apps.cars.models import CarModel
#
#
# def car_filter(query:QueryDict) -> QuerySet:
#     qs = CarModel.objects.all()
#
#     for k, v in query.items():
#         match k:
#             case 'price_gt': qs.filter(price__gt=v)
#             case 'brand_contains': qs.filter(brand__contains=v)
#             case _:
#                 raise ValidationError(f"Invalid value for {k}")
#     return qs