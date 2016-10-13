# -*- coding:utf-8 -*-


from boss.models import Vehicle
from boss.forms import VehicleAddForm, VehicleFindForm 

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@login_required
def add_vehicle(request):
    """add vehicle info"""
    if request.method != "POST":
        return JsonResponse({"is_ok": 0,
                             "msg": u"请求类型错误"
                             })
    form = VehicleAddForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"is_ok": 0,
                             "msg": form.errors.values()[0][0]
                             })
    vehicle_id = form.cleaned_data["vehicle_id"]
    password= form.cleaned_data["password"]
    try:
        Vehicle.objects.create(vehicle_id=vehicle_id, password=password)
    except Exception as e:
        return JsonResponse({"is_ok": False,
                             "msg": "add fail"
                             })

    return JsonResponse({"is_ok": True,
                         "msg": "add successful"
                         })
    
@csrf_exempt
def find_vehicle(request):
    """find vehicle password by vehicle's id"""
    if request.method != "POST":
        return JsonResponse({"is_ok": 0,
                             "msg": u"请求类型错误"
                             })
    form = VehicleFindForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"is_ok": 0,
                             "msg": form.errors.values()[0][0]
                             })
    vehicle_id = form.cleaned_data["vehicle_id"]
    try:
        password = Vehicle.objects.filter(vehicle_id=vehicle_id).values_list("password")
    except Exception as e:
        return JsonResponse({"is_ok": False,
                             "msg": "find fail"
                             })
    if password:
        return JsonResponse({"is_ok": True,
                             "msg": password[0][0]
                             })
    return JsonResponse({"is_ok": True,
                         "msg": u"we don't have this record" 
                         })
