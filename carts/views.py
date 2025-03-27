
from django.shortcuts import render,redirect
from carts.models import Cart
from goods.models import Products


def cart_add(request,product_slug):
    product = Products.objects.get(slug=product_slug)
     
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
 
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
 
    return redirect(request.META['HTTP_REFERER'])
             
            


    
def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")
 
    cart = Cart.objects.get(id=cart_id)
 
    cart.quantity = quantity
    cart.save()
    
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)
 
    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }
 
    return JsonResponse(response_data)
 
 
 
    
   
def cart_remove(request,cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
    
    