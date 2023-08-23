from django.http import Http404
from django.shortcuts import render
from store.models import *
from images.models import *
from django.views.decorators.csrf import csrf_exempt
from math import ceil

def page_about(request):
    return render(request, "about.html", {"active_url": "/about"})

def page_contacts(request):
    return render(request, "contact.html", {"active_url": "/contact"})

def page_services(request):
    all_services = [item.get_cells() for item in Service.objects.all()]
    return render(request, "services.html", {"service_list": all_services, "active_url": "/services"})

def page_service(request, service_name):
    service = [item for item in Service.objects.all() if item.name == service_name][0].get_cells()
    return render(request, "service.html", {"service": service})

def main_page(request):
    all_catalogs = [item.get_cells() for item in Catalog.objects.all()]
    all_slides = [item.get_cells() for item in Main_slider.objects.all()]
    return render(request, "main.html", {"catalog_list": all_catalogs, "all_slides": all_slides, "active_url": "/"})

@csrf_exempt
def page_products(request, catalog, page_number=1):
    # cost_render - for render "value" in <input> 
    cost_min_render = ""
    cost_max_render = ""
    try:
        header = [item.render_name for item in Catalog.objects.all() if item.get_cells()["name"] == catalog][0]
    except:
        header = None
        raise Http404("Страница не найдена")

    if request.method == "GET": # product with default price
        all_products = [item for item in Product.objects.all() if item.catalog.name == catalog]
    if request.method == "POST": # products with a certain price
        cost_min = request.POST.get("cost-min")
        cost_max = request.POST.get("cost-max")

        if cost_min == "":
            cost_min = 1
        else:
            cost_min = int(cost_min)
            cost_min_render = cost_min

        if cost_max == "":
            cost_max = 1000000000000
        else:
            cost_max = int(cost_max)
            cost_max_render = cost_max
    
        all_products = [item for item in Product.objects.all() if item.catalog.name == catalog and int(item.price) >= cost_min and int(item.price) <= cost_max]
    # limit, so as not to slow down when loading the page
    limit = 40
    number_pages = ceil(len(all_products) / limit)
    if len(all_products) > limit:
        all_products = all_products[limit * (page_number - 1):page_number * limit]

    # add id in info
    index = 0
    for item in all_products:
        all_products[index] = item.get_cells()
        all_products[index]["ID"] = item.id
        index += 1

    catalogs_list = [item.get_cells() for item in Catalog.objects.all()]
    return render(request, "products.html", {"catalogs_list": catalogs_list,
                                             "all_products": all_products, 
                                             "title": catalog,
                                             "catalog": catalog,
                                             "cost_max_render": cost_max_render, 
                                             "cost_min_render": cost_min_render,
                                             "header": header,
                                             "number_pages": range(1, number_pages + 1),
                                             "page_number": page_number,
                                             })

@csrf_exempt
def page_products_subdirectories(request, catalog, subdirectory, page_number=1):
    # cost_render - for render "value" in <input>
    cost_min_render = ""
    cost_max_render = ""

    try:
        header = [item.render_name for item in Catalog.objects.all() if item.get_cells()["name"] == catalog][0]
    except:
        header = None
        raise Http404("Страница не найдена")

    if request.method == "GET": # product with default price
        all_products = [item for item in Product.objects.all() if item.catalog.name == catalog and subdirectory in [ sub.name for sub in list(item.subdirectories.all())]]
    if request.method == "POST": # products with certain price
        cost_min = request.POST.get("cost-min")
        cost_max = request.POST.get("cost-max")

        if cost_min == "":
            cost_min = 1
        else:
            cost_min = int(cost_min)
            cost_min_render = cost_min

        if cost_max == "":
            cost_max = 100000000000000000000
        else:
            cost_max = int(cost_max)
            cost_max_render = cost_max
    
        all_products = [item for item in Product.objects.all() if item.catalog.name == catalog and int(item.price) >= cost_min and int(item.price) <= cost_max and subdirectory in [ sub.name for sub in list(item.subdirectories.all())]]

    # limit, so as not to slow down when loading the page
    limit = 40
    number_pages = ceil(len(all_products) / limit)
    if len(all_products) > limit:
        all_products = all_products[limit * (page_number - 1):page_number * limit]

    # add id in info 
    index = 0
    for item in all_products:
        all_products[index] = item.get_cells()
        all_products[index]["ID"] = item.id
        index += 1

    # getting directories to display a list of directories
    catalogs_list = [item.get_cells() for item in Catalog.objects.all()]
    
    return render(request, "products.html", {"catalogs_list": catalogs_list,
                                             "all_products": all_products,
                                             "title": subdirectory,
                                             "catalog": catalog,
                                             "subdirectory": subdirectory,
                                             "cost_max_render": cost_max_render,
                                             "cost_min_render": cost_min_render,
                                             "header": header,
                                             "number_pages": range(1, number_pages + 1),
                                             "page_number": page_number,
                                             })

# product page
def page_product(request, ID):
    product = [product for product in Product.objects.all() if product.id == ID][0].get_cells()
    return render(request, "product.html", {"product": product})