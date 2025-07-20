from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import MenuItem, Cart, Cartitem, Person
from .forms import CustomUserForm

# Create your views here.
def index(request):
    return render(request,'index.html')
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

def food_items_view(request):
    items = MenuItem.objects.all()
    return render(request, 'order.html', {'menu_items': items})
@login_required
def menu_view(request):
    menu_items = MenuItem.objects.select_related('restaurant').all()
    return render(request, 'menu.html', {'menu_items': menu_items})
def SignUp(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('order')  
    else:
        form = CustomUserForm()
    
    return render(request, 'signup.html', {'form': form})

