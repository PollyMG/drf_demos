import permission as permission
from rest_framework import views as api_views, serializers, permissions
from rest_framework import generics as api_views

# This should be in file 'serializers.py'
from rest_framework.response import Response

from drf_demos.api.models import Product, Category


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ('id', 'name')
        fields = '__all__'


class IdAndNameProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('id', 'name')
        fields = '__all__'


class FullCategorySerializer(serializers.ModelSerializer):
    product_set = IdAndNameProductSerializer(many=True)

    class Meta:
        model = Category
        # fields = ('id', 'name')
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    category = IdAndNameCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


# class ManualProductsListView(api_views.APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products,many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.validated_data)
#             return Response(status=201)
#         return Response(serializer.errors, status=201)


class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def list(self, request, *args, **kwargs):
        print(self.request.user)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CategoriesListView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

