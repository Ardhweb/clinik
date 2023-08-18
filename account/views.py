from django.shortcuts import render,HttpResponse,get_object_or_404,redirect

# Create your views here.
from .forms import UserForm, ProfileForm, AddressForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile, User

def register_new_user(request):
    form1 = UserForm(request.POST)
    form2 = AddressForm(request.POST)
    form3 = ProfileForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            new_user = form1.save(commit=True)
            add_address = form2.save(commit=True)
            profile = form3.save(commit=False)
            new_user.set_password(form1.cleaned_data['password'])
            new_user.save()

            print(new_user.username)

            add_address.save()

            print(add_address.city)
         
            profile.user = new_user
            profile.address = add_address
            profile.image = form3.cleaned_data['image']
            profile.save()
            print(profile.image)
        #return HttpResponse('Account and Address Created')
        return redirect('account:login')
    else:
        form1 = UserForm()
        form2 = AddressForm()
        form3 = ProfileForm()
    return render(request,'account/register.html',{'form1': form1,
    'form2':form2,'form3':form3})



from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    current_user = request.user
    user_id = current_user.id
    #print(user_id)
    if current_user.role == 'doctor':
        #user_info = get_object_or_404(User, id=user_id)
        user_info = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user_id)
        return render(request,'account/dynmicdashboard.html',{'user_info':user_info,'profile':profile})
    elif current_user.role == 'patient':
        user_info = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user_id)
        return render(request,'account/dynmicdashboard.html',{'user_info':user_info,'profile':profile})
    else:
        return HttpResponse("You Not Allowed Here")



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account:dashboard')
                    #return HttpResponse('Authenticated ''successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    #return HttpResponseRedirect(request,'log_out.html',context_instance = RequestContext(request))
    #return HttpResponse("Your are Loggedout now.")
    return render(request,"account/logged_out.html")