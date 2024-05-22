from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at')

    def validate(self, attrs):
        year_ = attrs['year']
        price_ = attrs['price']
        if year_ == price_:
            raise serializers.ValidationError({'details': f'{year_} is equal to {price_}'})
        return attrs

    def validate_year(self, year):
        if year == 2003:
            raise serializers.ValidationError({'details': f'year is equal to {year}'})
        return year


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year')








