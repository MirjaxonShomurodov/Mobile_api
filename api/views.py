from django.http import HttpRequest, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Mobile
from datetime import datetime

def add_product(reqeust: HttpRequest) :
    if reqeust.method == 'POST':
            data = json.loads(reqeust.body.decode('utf-8'))
            s = ''
            mom = ''
            for i in data['RAM']:
                if i.isdigit():
                    s+=i
                else:
                    break
            for i in data['memory']:
                if i.isalpha():
                     continue
                else:
                     mom+=i
            n = eval(mom)
            product = Mobile.objects.create(
                price=data['price'],
                img_url=data['img_url'],
                color=data['color'],
                ram=int(s),
                memory=int(n),
                name=data['name'],
                model=data['company']
            )
            return JsonResponse({'status': 'OK'})
    else:
          return HttpResponse("Method error")
    
def get_product(request: HttpRequest) -> JsonResponse:

        products = Mobile.objects.filter(model='Oppo')
        print(len(products))
        data = []
        for product in products:
            data.append(product.to_dict())
        return JsonResponse(data, safe=False)

def all_product(request:HttpRequest)->JsonResponse:
    product = Mobile.objects.all()
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse({"data":data})

def delete_product(request:HttpRequest,pk)->JsonResponse:
    product = Mobile.objects.get(id=pk)
    
    product.delete()
    return JsonResponse({'status':"200 OK"})

def name_product(request:HttpRequest,name:str) ->JsonResponse:
    product = Mobile.objects.filter(name__contains = name)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def color_product(request:HttpRequest,color:str) ->JsonResponse:
    product  =Mobile.objects.filter(color__contains = color)
    data = []
    for i in product:               
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def price_product(request:HttpRequest,price:float)->JsonResponse:
    product = Mobile.objects.filter(price__lte = price)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe = False)

def gte_product(request:HttpRequest,gte:float)->JsonResponse:
    product = Mobile.objects.filter(id_gte = gte)
    data = []
    for i in product:
         data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def lt_product(request:HttpRequest,lt:float)->JsonResponse:
    product = Mobile.objects.filter(id_lt = lt)
    data = []
    for i in product:
         data.append(i.to_dict())
    return JsonResponse(data,safe=True)

def gt_product(request:HttpRequest,gt:float)->JsonResponse:
     product = Mobile.objects.filter(id_gt = gt)
     data = []
     for i in product:
          data.append(i.to_dict())
     return JsonResponse(data,safe=False)

def price1_product(requset:HttpRequest,price1,price2)->JsonResponse:
    product = Mobile.objects.filter(price__gte=price1,  price_lte=price2)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def brind_product(request:HttpRequest,brind)->JsonResponse:
    product = Mobile.objects.filter(brand=brind)
    all = []
    for i in product:
        all.append(i.to_dict())
    return JsonResponse(all,safe=False)

def iendswith_product(request:HttpRequest, kp:str) ->JsonResponse:
    product = Mobile.objects.filter(description__icontains=kp)
    data = []
    for i in product:
         data.append(i.to_dict())
    return JsonResponse(data, safe=False)

def istartswith(request:HttpRequest,istartswith:str)->JsonResponse:
    product = Mobile.objects.filter(description__istartswith=istartswith)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def endswith_product(request:HttpRequest,endswith:str)->JsonResponse:
    product = Mobile.objects.filter(description_endswith = endswith)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def year_product(request:HttpRequest,year)->JsonResponse:
    product = Mobile.objects.filter(pub_date_year = year)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def time_product(request:HttpRequest,time)->JsonResponse:
    product = Mobile.objects.filter(pub_date_time = time)
    data = []
    for i in product:
        data.append(i.to_dict())
    return JsonResponse(data,safe=False)

def update_product(request:HttpRequest,pk):
    if request.method=='POST':
        product = Mobile.objects.get(id=pk)
        
        data = json.loads(request.body.decode('utf-8'))
        product.price==data.get('price',product.price),
        product.img_url==data.get('img_url',product.price),
        product.color==data.get('color',product.color),
        product.ram==data.get('RAM',product.ram),
        product.memory==data.get('memory',product.memory),
        product.name==data.get('name',product),
        product.model==data.get('company',product.model)
        product.save()
    return JsonResponse({'status':'200'})
