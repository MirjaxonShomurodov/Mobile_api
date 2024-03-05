from django.urls import path
from .views import(
     add_product,get_product,
     all_product,name_product,
     price_product,color_product,
     delete_product,price1_product,
     brind_product,iendswith_product,
     istartswith,get_product_id,lt_product,
     gt_product,lst_models,
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
    path('price1/<price0><price2>/',price1_product),
    path('<brind>/all/',brind_product),
    path('iendswith/<iendswith>/',iendswith_product),
    path('istartswith/<istartswith>',istartswith),
    path('gte/<int:pk>',get_product_id),
    path('price_lt/<lt>/',lt_product),
    path('price_gt/<gt>/',gt_product),
    path('update/<int:pk>',update_product),
    path('models/', lst_models),
    path('models/<str:name>', get_name)
]
