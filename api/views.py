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

def get_product_id(request:HttpRequest,pk:int)->JsonResponse:
    product = Mobile.objects.get(id = pk)
    return JsonResponse(product.to_dict())



def lst_models(request: HttpRequest) -> JsonResponse:
    """get all models"""
    try:
        product = Mobile.objects.all()
        data = []
        for i in product:
            data.append(i.to_dict()['model'])
        data = list(set(data))
    except:
        return JsonResponse({"data":"not found"})
    return JsonResponse(data=data, safe=False)
def update_product(request:HttpRequest,id:int):
    if request.method == "POST":
            data = request.body.decode('utf-8')
            data = json.loads(data)
            item = Mobile.objects.filter(id=id) 
            item.update(
                name = data['name'],
                model = data['model'],
                color = data['color'],
                ram = data['ram'],
                memory = data['memory'],
                price = data['price'], 
                img_url = data['url'], 
            )
            obj = Mobile.objects.all()
            ruyxat = []
            for item in obj:
                ruyxat.append(item.to_dict())
            return JsonResponse({"smartphes":ruyxat}, safe=False)
def get_name(request: HttpRequest, name: str) -> JsonResponse:
    """get product by name"""
    # Get product by name
    try:
        product = Mobile.objects.filter(model__contains = name)
        data = []
        for i in product:
            data.append(i.to_dict())
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    # Return response
    return JsonResponse(data=data, safe=False )