from django.urls import path
from .views import(
     add_product,get_product,
     all_product,name_product,
     price_product,color_product,
     delete_product,get_product_id,lst_models,
     get_name,update_product,
)

urlpatterns = [
    path('add/',add_product),
    path('get/',get_product),
    path('all/',all_product),
    path('delete/<int:pk>',delete_product),
    path("name/<name>/",name_product),
    path("color/<color>/",color_product),
    path('price/<price>/',price_product),
    path('gte/<int:pk>',get_product_id),
    path('update/<int:pk>',update_product),
    path('models/', lst_models),
    path('models/<str:name>', get_name)
]
