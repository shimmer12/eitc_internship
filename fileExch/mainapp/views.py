from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageUploadForm # new 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from .models import Image

@login_required(login_url='login')
def index(request):
    selected_category = request.GET.get('category', '')  # Get the selected category from the URL parameters
    data = Image.objects.all()
    user = request.user  # Get the logged-in user
    access_levels = user.access_levels.all()  # Get the access levels for the user
    access_levels_names = [level.name for level in access_levels]  # Get the names of the access levels
    print(access_levels_names)
    print(access_levels)
    context = {
        'data': data,
        'selected_category': selected_category,
        'username': user.username,
        'access_levels': access_levels_names,
    }
    return render(request, "display.html", context)




@login_required(login_url='login') 
def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_files')
    else:
            form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def editView(request, id):
    image = Image.objects.get(id=id)  # Get the Image instance
    form = ImageUploadForm(instance=image)  # Instantiate the ImageForm with the Image instance

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=image)  # Bind the submitted data to the form

        if form.is_valid():
            form.save()  # Save the updated form data
            return redirect('/')  # Redirect to the desired URL after successful update

    return render(request, 'edit.html', {'form': form})
def update(request,id):
    form = Image.objects.get(id=id)
    form = ImageUploadForm(request.POST,instance=form)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})
def destroy(request,id):
    employee = Image.objects.get(id=id)
    employee.delete()
    return redirect('/')



from django.contrib.auth import authenticate, login, logout
from mainapp.forms import UserRegisterForm, AuthenticationForm

from .models import AccessLevel

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            access_level = form.cleaned_data.get('access_level')
            access_level_obj = AccessLevel.objects.get(name=access_level)
            user.save()  # Save the user object to assign an ID
            user.access_levels.add(access_level_obj)  # Add the access level
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form, 'title': 'register here'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('display_files')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'Log in'})

def logout_view(request):
    logout(request)
    return redirect('login')
