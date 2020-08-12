from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.Product_det.as_view()),
    path('api/<int:pk>/',views.ProductIndividual.as_view()),
    path('', views.ProductList.as_view()),
    path('MostViewed/', views.MostViewed.as_view()),
    path('Details/<int:ProId>/', views.ProductDetails.as_view()),
    path('Location/<int:ProId>/', views.LocationOfProduct.as_view()),
    path('ClickedIt/<int:ProId>/', views.ClickedIt.as_view()),

]