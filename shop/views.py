from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView

from .forms import SubproductForm, UserForm, RegForm, UserFormRegister, ChangePasswordForm
from .models import Category, Product, Subproduct, Homework, ExtendUser, DataModelUser
import requests
import json


def Rstring():
    res = requests.get('https://jsonplaceholder.typicode.com/users')
    data = res.json()
    print(data[0])


# Create your views here.


def saveuser_db(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    Rstring()
    user = DataModelUser.objects.get(login=login)
    if user:
        if check_password(password, user.password):
            print(password)
            return HttpResponse('Ты вошел')

    return render(request, 'shop/product/list.html')

    # data = request.POST
    # print(data)
    # valid_data = {'login': request.POST.get('login'), 'password': request.POST.get('password')}
    # user = DataModelUser()
    # user.login = request.POST.get('login')
    # requestPassword = request.POST.get('password')
    # dbPassword = DataModelUser.objects.
    # user.password = make_password(password)
    # # print(user)
    # if user.login:
    #     db_users = DataModelUser.objects.filter(login=user.login)
    #     if db_users:
    #         print('Пользователь существует', db_users)
    #         # db_password = [db_user.password for db_user in db_users][0]
    #         # for db_user in db_users:
    #         #     db_password = db_user.password
    #         # print([db_user.password for db_user in db_users][0])
    #         # # print(is_password_usable(password))
    #         # # print(user.password)
    #         # # print(is_password_usable([db_user.password for db_user in db_users][0]))
    #         # if check_password(password, [db_user.password for db_user in db_users][0]):
    #         #     print('Пользователь с таким логином и паролем уже существует в системе', db_users)
    #         # else:
    #         #     print('Существует пользователь с таким логином', db_users)
    #     else:
    #         user.save()


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    content = {'category': category,
               'categories': categories,
               'products': products,
               'warning': 'Должно быть не меньше 6 символов и не содержать цифр'}
    return render(request, 'shop/product/list.html', content)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    content = {'product': product}
    return render(request, 'shop/product/detail.html', content)


def index(request):
    request.session['Sancho'] = 'Sashcka'
    request.session['Sancho1'] = 'Sashcka1'
    request.session.set_expiry(20)
    # dictSes=dict(request.session)
    # print(request.session['Sancho1'])
    # arr=[]
    # for i in dictSes:
    #     arr.append(i)
    #     arr.append(dictSes[i])
    # print(arr)
    s = request.session['key']=100
    response = render(request, 'shop/base.html', {'s': s})
    response.set_cookie('kolya', '2', samesite='Strict')
    return response

    # if request.method == 'POST':
    #     if request.session.test_cookie_worked():
    #         #request.session.delete_test_cookie()
    #         return HttpResponse("You're logged in.")
    #     else:
    #         return HttpResponse("Please enable cookies and try again.")
    #

    data = request.POST
    dataDbUser = ExtendUser.objects.all()
    R = ExtendUser.objects.all()
    # print(dataDbUser)3
    if request.POST:
        # request.session.set_test_cookie()
        name = data['login']
        if len(name) < 6:
            return render(request, 'shop/base.html', {'error': 'Логин должен быть хотя бы 6 символов', 'color': 'red'})
        elif not name.isalpha():
            return render(request, 'shop/base.html', {'error': 'Логин должен состоять только из букв', 'color': 'red'})
        else:
            return render(request, 'shop/base.html',
                          {'success': 'OK', 'color': 'green', 'dataDbUser': dataDbUser, 'R': R})
    return render(request, 'shop/base.html', {'R': R})


class SubproductCreate(View):
    def get(self, request):
        form = SubproductForm()
        return render(request, 'shop/product/subproduct.html', context={'form': form})

    def post(self, request):
        form = SubproductForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Subproduct.objects.create(name=cleaned_data['name'],
                                      image=cleaned_data['image'],
                                      description=cleaned_data['description'],
                                      price=cleaned_data['price'])
            return redirect('/')
        else:
            return render(request, 'shop/product/subproduct.html', context={'form': form})


# def subproduct_view(request):
#     form = SubproductForm()
#     if request.method == 'POST':
#         form = SubproductForm(request.POST, request.FILES)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             Subproduct.objects.create(name=cleaned_data['name'],
#                                       image=cleaned_data['image'],
#                                       description=cleaned_data['description'],
#                                       price=cleaned_data['price'])
#     return render(request, 'shop/product/subproduct.html', context={'form': form})


# def subproduct_view1(request):
#     """ Написать комментарии, чем отличается от предыдущей вьюхи """
#     form = SubproductForm(request.POST or None,  request.FILES or None)
#     if request.method == 'POST' and form.is_valid():
#         print(form.cleaned_data)
#         cleaned_data = form.cleaned_data
#         Subproduct.objects.create(name=cleaned_data['name'],
#                                   image=cleaned_data['image'],
#                                   description=cleaned_data['description'],
#                                   price=cleaned_data['price'])
#     return render(request, 'shop/product/subproduct.html', context={'form': form})

def testform(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'shop/test/testform.html', context={'form': form})
    if request.method == 'POST':
        data = request.POST
        print(data)
        return render(request, 'shop/product/list.html')


def hwform(request):
    if request.method == 'GET':
        my_form = RegForm()
        return render(request, 'shop/test/HWform.html', context={'RegForm': my_form})
    if request.method == 'POST':
        my_form = RegForm(request.POST, request.FILES)
        # print(request.POST)
        # print(request.FILES)
        if my_form.is_valid():
            cleaned_data = my_form.cleaned_data
            # print(cleaned_data)
            Homework(login=cleaned_data['login'],
                     password=cleaned_data['password'],
                     surname=cleaned_data['surname'],
                     phone=cleaned_data['phone'],
                     description=cleaned_data['description'],
                     reg_date=cleaned_data['reg_date'],
                     check=cleaned_data['check'],
                     radio=cleaned_data['radio'],
                     file=cleaned_data['file'],
                     image=cleaned_data['image'],
                     ).save()
            return redirect('/')
        return render(request, 'shop/test/HWform.html', context={'RegForm': my_form})


class ShopLoginView(LoginView):
    template_name = 'shop/user/login.html'
    redirect_field_name = 'shop/user/profile.html'


@login_required
def profile(request):
    return render(request, 'shop/user/profile.html')


class ShopLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'shop/product/list.html'


class ShopUserRegisterView(CreateView):
    model = ExtendUser
    template_name = 'shop/user/user_register.html'
    form_class = UserFormRegister
    success_url = reverse_lazy('shop:product_list')


@login_required
def change_password(request):
    if request.method == 'POST':
        passwords = request.POST
        user = request.user
        old_password = passwords['old_password']
        new_password1 = passwords['new_password1']
        new_password2 = passwords['new_password2']
        if check_password(old_password, user.password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
    form = ChangePasswordForm()
    context = {'form': form}
    return render(request, 'shop/user/change_password.html', context)
