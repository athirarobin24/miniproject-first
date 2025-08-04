from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login,logout
from .models import MenuItem, Cart, Cartitem, Person
from .forms import CustomUserForm
from django.contrib import messages


# Create your views here.
def index(request):
    data=MenuItem.objects.all()[:10]
    return render(request,'index.html',{'data':data})
def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request,'booking.html')
def contact(request):
    return render(request,'contact.html')
def menu(request):
    return render(request,'menu.html')
def service(request):
    return render(request,'service.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')


@login_required(login_url='login')
def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('menu_item_id')
        quantity = int(request.POST.get('quantity', 1))
        menu_item = get_object_or_404(MenuItem, id=item_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = Cartitem.objects.get_or_create(cart=cart, menu_item=menu_item)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return redirect('payment')
    return redirect('menu')
@login_required
def payment_view(request):
    return render(request, 'payment.html')
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

