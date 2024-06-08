
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import FAQ,Course
from .forms import UserRegisterForm,UserLoginForm
def index_view(request):
    faqs = FAQ.objects.all()
    python = Course.objects.get(title='Python')
    go = Course.objects.get(title='Go')
    html_css = Course.objects.get(title='HTML/CSS')
    design = Course.objects.filter(title='UI/UX Design')
    js = Course.objects.filter(title='JavaScript')

    return render(request,'app/index.html',
                  {'faqs':faqs,
                           'python': python,
                            'go':go,
                            'html_css':html_css,
                            'design':design,
                            'js':js

    })





def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_view')
        else:
            print("Форма не валидна:", form.errors)
    else:
        form = UserRegisterForm()

    return render(request, 'app/user_register.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)


        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,usename=username,password=password)

                if user:
                    login(request,user)
                return redirect('index_view')

    form = UserLoginForm()

    return render(request, 'app/user_login.html',{'form':form})



def user_logout_view(request):
    logout(request)
    return redirect('index_view')

