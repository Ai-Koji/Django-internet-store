"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path
import store.views as store
import form.views as form

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", store.main_page, name="main"),
    path("products/page-<int:page_number>/<str:catalog>/", store.page_products, name="products"),
    path("products/page-<int:page_number>/<str:catalog>/<str:subdirectory>/", store.page_products_subdirectories, name="subdirectory"),
    path("product/<int:ID>", store.page_product, name="product"),
    path("about/", store.page_about, name="about"),
    path("contact/", store.page_contacts, name="contact"),
    path("services/", store.page_services, name="services"),
    path("services/<str:service_name>/", store.page_service, name="service"),
    path("send_form/<str:catalog>", form.get_form)
]
