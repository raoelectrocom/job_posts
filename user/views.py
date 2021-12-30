# djagno imports
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# util imports
from user.forms import NewUserForm, ProfileForm


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render (
        request=request,
        template_name="user/register.html",
        context={"form": form}
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name="user/login.html",
        context={"login_form":form}
    )


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")


def edit_profile(request):
    if request.method=="POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated succesfully.")
            return redirect("homepage")
    else:
        form=ProfileForm(instance=request.user)
    return render(request, "user/edit_profile.html", {'form':form})