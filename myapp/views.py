from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import UserForm
from .models import UserModel

# Create 
def create(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created')
            return redirect('read')
    context = {
        'form':form
    }
    return render(request, 'myapp/create.html', context)

# Read
def read(request):
    user_data = UserModel.objects.all()
    context = {
        'user_data':user_data
    }
    return render(request, 'myapp/read.html', context)

# Update
def update(request, pk):
    get_user_data = get_object_or_404(UserModel, pk=pk)
    form = UserForm(instance=get_user_data)
    if request.method == "POST":
        form = UserForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('read')
    context = {
        'form':form
    }
    return render(request, 'myapp/update.html', context)

# Delete user
def delete(reqest, pk):
    get_user = get_object_or_404(UserModel, pk=pk)
    get_user.delete()
    messages.error(reqest, 'User deleted')
    return redirect('/')