from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import signupForm, AddRecordForm
from .models import Record


def zer0Point(req):
    return render(req,'app/zer0Point.html')

def home(req): 

    records = Record.objects.all()
    


    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req, username=username, password= password)
        if user is not None:
            login(req, user)
            messages.success(req,"You have been Logged In !!! ")
            return redirect('home')
        else:
            messages.success(req,"There was an error logging in !!! ")
            return redirect('home')
    else:
        return render(req,'app/index.html',{'records':records})


def login_user(req): 
    pass


def logout_user(req):
    logout(req)
    messages.success(req,"You have been Logged Out !!! ")
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = signupForm()
    return render(request, 'app/signup.html', {'form':form})

def user_record(req,pk):
    if req.user.is_authenticated:
        customer_recod = Record.objects.get(id=pk) 
        return render(req, 'app/record.html', {'customer_record':customer_recod})
    else:
        messages.success(req,"You have to login first !!! ")
        return redirect('home')


def delete_user(req,pk): 
    if req.user.is_authenticated:
        deleteting_user = Record.objects.get(id=pk)
        deleteting_user.delete()

        messages.success(req,"Record has been deleted !!! ")
        return redirect('home')
    else:
        messages.success(req,"You have to login first !!! ")
        return redirect('home')
    



def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'app/add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_record(req, pk):
    if req.user.is_authenticated:
         current_record = Record.objects.get(id=pk)
         form = AddRecordForm(req.POST or None, instance=current_record)
         if form.is_valid():
             form.save()
             messages.success(req, "Record Updated...")
             return redirect('home')
         return render(req, 'app/update_record.html', {'form':form})  
    else:
        messages.success(req, "You Must Be Logged In...")
        return redirect('home')