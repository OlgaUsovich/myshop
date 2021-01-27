
from django.urls import path
from .views import product_detail, SubproductCreate, testform, ShopLoginView, hwform, profile, ShopLogoutView, \
    ShopUserRegisterView, saveuser_db, change_password
from .views import product_list
from . import views

app_name = 'shop'
urlpatterns = [
    path('saveuser/', saveuser_db, name='saveuser'),
    path('accounts/register', ShopUserRegisterView.as_view(), name='register'),
    path('accounts/change_password/', change_password, name='change_password'),
    path('accounts/logout/', ShopLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', ShopLoginView.as_view(), name='login'),
    path('homework/', hwform),
    path('testform/', testform),
    path('subprod/', SubproductCreate.as_view(), name='subproduct'),
    path('api/', views.index),
    path('', product_list, name='product_list'),
    path(r'^(P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),
]
