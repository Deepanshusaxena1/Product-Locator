from django.shortcuts import redirect, get_list_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from rest_framework import generics, permissions

# Create your views here.
from rest_framework.decorators import permission_classes

from .models import Product
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView


class Product_det(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductIndividual(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ProductList.html'

    def get(self, request):
        queryset = Product.objects.all()
        return Response({'Products': queryset})


class MostViewed(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ProductList.html'

    def get(self, request):
        queryset = Product.objects.order_by('-Product_On_Click_Count')
        if queryset.count() < 10:
            return Response({'Products': queryset})
        else:
            queryset = Product.objects.order_by('-Product_On_Click_Count')[10]
            return Response({'Products': queryset})


class ProductDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ProductDetails.html'

    def get(self, request, ProId):
        queryset = Product.objects.get(Product_Id=ProId)
        # array
        return Response({'Product': queryset})


class LocationOfProduct(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'LocationOfProduct.html'

    def get(self, request, ProId):
        queryset = Product.objects.get(Product_Id=ProId)
        return Response({'LocateProduct': queryset})


class ClickedIt(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'LocationOfProduct.html'
    # @method_decorator(never_cache, name='dispatch')
    def get(self, request, ProId):
        currentobj = Product.objects.get(Product_Id=ProId)
        # return Response({'LocateProduct': queryset})
        currentobj.Product_On_Click_Count = currentobj.Product_On_Click_Count + 1
        currentobj.save()
        # return redirect(LocationOfProduct,ProId)
        return redirect("../../Details" + "/" + str(ProId))