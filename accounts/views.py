from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        raw_password2 = request.POST.get('password2')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if raw_password != raw_password2:
            message = '패스워드가 일치하지 않습니다.'
            context = {
                'message': message,
                'username': username,
                'name': name,
                'email': email,
            }
            return render(request, 'accoutns/signup.html', context)

        else:
            try:
                user = User.objects.get(username=username)
                message = '이미 사용되고 있는 아이디입니다.'
                context = {
                    'message': message,
                    'username': username,
                    'name': name,
                    'email': email,
                }
                return render(request, 'accounts/signup.html', context)

            except:
                user = User.objects.create_user(username=username, password=raw_password)
                user.email = email
                user.first_name = name
                user.save() 
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
    
    return render(request, 'accounts/signup.html', {'message':''})



def super_login(request):

    if not request.user.username == 'admin':
        return redirect('/accounts/login/')

    users = User.objects.all()
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        
        if authenticate(username='admin', password=password):
            user = User.objects.get(id=user_id)
            login(request, user)
        
        return redirect('/')
    
    context = {
        'users': users,
    }
    return render(request, 'accounts/super_login.html', context)

