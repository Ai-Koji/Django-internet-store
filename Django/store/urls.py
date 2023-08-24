from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main"),
    path("products/page-<int:page_number>/<str:catalog>/", page_products, name="products"),
    path("products/page-<int:page_number>/<str:catalog>/<str:subdirectory>/", page_products_subdirectories, name="subdirectory"),
    path("product/<int:ID>", page_product, name="product"),
    path("about/", page_about, name="about"),
    path("contact/", page_contacts, name="contact"),
    path("services/page-<int:page_number>/", page_services, name="services"),
    path("service/<str:service_name>/", page_service, name="service"),
]