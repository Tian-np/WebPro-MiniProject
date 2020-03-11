from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render
from pkg_resources import require

from homepage.models import Faculty, Food, Restaurant, RestaurantFood

# Create your views here.


def index(request):
    search = request.GET.get('inputSearch', '')
    faculty = Faculty.objects.all()
    classes = Restaurant.objects.filter(
        name__icontains=search
    )
    return render(request, template_name='index.html',
                  context={
                      'search': search,
                      'classes': classes,
                      'faculty': faculty}
                  )


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)

        if user:
            # login(request, user)
            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    return render(request, template_name='login.html', context=context)


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login')


def add(request):
    return render(request, template_name='add.html')


# def resf_list(request, res_id):

#     res = Restaurant.objects.get(pk=res_id)
#     list_f = Restaurant_food.objects.filter(
#         restaurant=res_id
#     )
#     return render(request, 'datails.html', context={
#         'res_f': res,
#         'list_f': list_f
#     })
