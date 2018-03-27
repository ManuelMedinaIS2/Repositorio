from django.shortcuts import render

def home(request):
    """
    Página Inicial.

    """
    return render(request,'login.html')


def login_view(request):
    """
    Página de Login.
    """
    next_url = ''
    if request.GET:
        next_url = request.GET.get('next', '')

    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('passsword')
            exist = User.objects.filter(username=username).exists()
            user = authenticate(username=username, password=password)

            if exist:
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        if next_url:
                            return redirect(next_url)
                        else:
                            return redirect('login:home')
                    else:
                        messages.add_message(request, messages.WARNING,
                                             'Usuario -%s- existe pero no está activo.' % username)
                else:
                    messages.add_message(request, messages.ERROR, 'Credenciales incorrectos.')
            else:
                messages.add_message(request, messages.ERROR, 'Usuario -%s- no existe.' % username)
        return render(request, 'login.html', {'next': next_url})
    else:
        if next_url:
            return redirect(next_url)
        else:
            return redirect('login:home')


def logout_view(request):
    """
        Cierra sesión de usuario.
    """
    logout(request)
    return redirect('login:home')
