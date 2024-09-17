from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
import random
import string
from .forms import CustomUserCreationForm
from .models import CustomUser, Category, Subcategory, Product

def home(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    context = {"categories":categories,
               "products":product 
               }
    return render(request, "store/index.html",context)
 
 
def product(request, slug):
    product = Product.objects.get(slug=slug)
    upsell_products = Product.objects.filter(subcategory=product.subcategory).exclude(id=product.id)[:10]
    
    context={
        "product":product,
        'upsell_products': upsell_products
    }
    return render(request,"store/product_detail.html",context)

def category(request,slug):
    
    return render(request,"store/category.html")











def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in successfully")
            return redirect("home")
        else:
            messages.error(request,"There was an error! check your phone number and password and try again")
            return redirect("login")
    else:
        return render(request,"store/login.html")


def generate_unique_username(base):
    """
    Generates a unique username by appending random digits to the base.
    """
    username = base
    while CustomUser.objects.filter(username=username).exists():
        username = f"{base}{''.join(random.choices(string.digits, k=4))}"
    return username

from django.contrib.auth import login

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user yet

            # Get email and phone from form data
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')

            # Generate a base username (use email prefix or phone)
            base_username = email.split('@')[0] if email else phone
            username = generate_unique_username(base_username)

            # Assign the generated username to the user
            user.username = username

            # Save the user after assigning the username
            user.save()

            # Explicitly specify the backend
            backend = 'store.backends.EmailOrPhoneBackend'  # Use your custom backend
            login(request, user, backend=backend)

            return redirect('home')  # Redirect to home or success page
    else:
        form = CustomUserCreationForm()

    return render(request, 'store/registration.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect("home")