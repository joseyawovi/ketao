from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    
    #get the products
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    context = {"cart_products":cart_products,
               "quantities":quantities,
               }
    return render(request,'cart/cart_view.html', context)

def cart_add(request):
      #get the cart
    cart = Cart(request)
    
    #test for post
    if request.POST.get('action')== 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #look for the product in DB
        
        product = get_object_or_404(Product,id=product_id)
        #save the session
        cart.add(product=product,quantity=product_qty)
        #return response
        #response = JsonResponse({'Product Name':product.name})
        #get cart quantity
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty':cart_quantity})
        return response

def cart_delete(request):
    pass
def cart_update(request):
    pass