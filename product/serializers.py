from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=150)
    slug=serializers.SlugField(max_length=200)
    description=serializers.CharField()
    price=serializers.DecimalField(default=0.00,max_digits=7,decimal_places=2)
    discount=serializers.DecimalField(default=0.00,max_digits=4,decimal_places=2)
    porcia=serializers.CharField(max_length=150,default=0)
    category_id=serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.slug=validated_data.get('slug',instance.slug)
        instance.description=validated_data.get('description',instance.description)
        instance.price=validated_data.get('price',instance.price)
        instance.discount=validated_data.get('discount',instance.discount)
        instance.porcia=validated_data.get('porcia',instance.porcia)
        instance.category_id=validated_data.get('category_id',instance.category_id)

        instance.save()
        return instance
  