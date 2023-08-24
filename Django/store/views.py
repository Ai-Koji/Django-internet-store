from django.http import Http404
from django.shortcuts import render
from store.models import *
from images.models import *
from django.views.decorators.csrf import csrf_exempt
from math import ceil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

limit = 1

def page_about(request):
    return render(request, "about.html", {"active_url": "/about"})

def page_contacts(request):
    return render(request, "contact.html", {"active_url": "/contact"})

def page_services(request):
    all_services = [item.to_dict() for item in Service.objects.all()]
    return render(request, "services.html", {"service_list": all_services, "active_url": "/services"})

def page_service(request, service_name):
    service = [item for item in Service.objects.all() if item.name == service_name][0].to_dict()
    return render(request, "service.html", {"service": service})

def main_page(request):
    all_catalogs = [item.to_dict() for item in Catalog.objects.all()]
    all_slides = [item.to_dict() for item in Main_slider.objects.all()]
    return render(request, "main.html", {"catalog_list": all_catalogs, "all_slides": all_slides, "active_url": "/"})

@csrf_exempt
def page_products(request, catalog, page_number=1):
    try:
        header = Catalog.objects.get(name=catalog).render_name
    except Catalog.DoesNotExist:
        raise Http404("Страница не найдена")

    products_query = Product.objects.filter(catalog__name=catalog)
    cost_min = ""
    cost_max = ""
    if request.method == "POST":
        try:
            cost_min = int(request.POST.get("cost-min", 1))
            all_products = all_products.filter(price__gte=cost_min)
        except:
            cost_min = ""
        try:
            cost_max = int(request.POST.get("cost-max", 100000000000000000000))
            all_products = all_products.filter(price__lte=cost_max)
        except:
            cost_max = ""

    paginator = Paginator(products_query, limit)
    
    try:
        all_products = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        all_products = paginator.page(1)
    
    all_products = [product.to_dict() for product in all_products]
    
    catalogs_list = [item.to_dict() for item in Catalog.objects.all()]
    return render(request, "products.html", {
        "catalogs_list": catalogs_list,
        "all_products": all_products,
        "title": catalog,
        "catalog": catalog,
        "cost_min_render": cost_min,
        "cost_max_render": cost_max,  
        "number_pages": range(1, paginator.num_pages + 1),
        "page_number": page_number,
    })

@csrf_exempt
def page_products_subdirectories(request, catalog, subdirectory, page_number=1):
    try:
        header = Catalog.objects.get(name=catalog).render_name
    except Catalog.DoesNotExist:
        header = None
        raise Http404("Страница не найдена")

    all_products = Product.objects.filter(
        catalog__name=catalog,
        subdirectories__name=subdirectory
    )
    cost_min = ""
    cost_max = ""
    if request.method == "POST":
        try:
            cost_min = int(request.POST.get("cost-min", 1))
            all_products = all_products.filter(price__gte=cost_min)
        except:
            cost_min = ""
        try:
            cost_max = int(request.POST.get("cost-max", 100000000000000000000))
            all_products = all_products.filter(price__lte=cost_max)
        except:
            cost_max = ""

    paginator = Paginator(all_products, limit)

    try:
        all_products = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        all_products = paginator.page(1)

    all_products = [product.to_dict() for product in all_products]
    
    catalogs_list = [item.to_dict() for item in Catalog.objects.all()]
    return render(request, "products.html", {
        "catalogs_list": catalogs_list,
        "all_products": all_products,
        "title": subdirectory,
        "catalog": catalog,
        "subdirectory": subdirectory,
        "header": header,
        "cost_min_render": cost_min,
        "cost_max_render": cost_max,  
        "number_pages": paginator.page_range,
        "page_number": page_number,
    })

# product page
def page_product(request, ID):
    product = [product for product in Product.objects.all() if product.id == ID][0].to_dict()
    return render(request, "product.html", {"product": product})