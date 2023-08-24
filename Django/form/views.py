from django.http import HttpResponse
from form.models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django_ratelimit.decorators import ratelimit
 
@ratelimit(key='ip', rate='20/2h')
@csrf_exempt
def get_form(request, catalog):
    if request.method == "POST":
        timeNow = str(datetime.now())
        if catalog == "offer":
            item = Offer(
                username = request.POST["name"], 
                email = request.POST["email"],
                phone_number = request.POST["phone"],
                product = request.POST["product"],
                time = timeNow[:timeNow.rfind(".")]
                )
            item.save()
            return HttpResponse(200)
        elif catalog == "service":
            item = ServiceOffer(
                username = request.POST["name"], 
                email = request.POST["email"],
                phone_number = request.POST["phone"],
                service_name = request.POST["service"],
                message = request.POST["message"],
                time = timeNow[:timeNow.rfind(".")]
                )
            item.save()
            return HttpResponse(200)
        elif catalog == "contact":
            item = Contact(
                username = request.POST["name"], 
                email = request.POST["email"],
                phone_number = request.POST["phone"],
                message = request.POST["message"],
                time = timeNow[:timeNow.rfind(".")]
                )
            item.save()
            return HttpResponse(200)
        elif catalog == "question":
            item = Question(
                username = request.POST["name"], 
                email = request.POST["email"],
                phone_number = request.POST["phone"],
                message = request.POST["message"],
                time = timeNow[:timeNow.rfind(".")]
                )
            item.save()
            return HttpResponse(200)

        else:
            return HttpResponse(500)
    else:
        return HttpResponse("error: only POST request")
