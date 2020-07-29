
from django.urls import path
from .views import home, createAccount, detailAccount, listAccount, updateAccount, deleteAccount, createStock, detailStock, listStock, updateStock, deleteStock

app_name = 'post'

urlpatterns = [
    path('',listStock, name='main'),
    path('account/create/',createAccount,name='createAcc'),
    path('account/detail/<int:pk>/',detailAccount,name='detailAcc'),
    path('account/list/',listAccount,name='listAcc'),
    path('account/detail/<int:pk>/update/',updateAccount,name='updateAcc'),
    path('account/detail/<int:pk>/delete/',deleteAccount,name='deleteAcc'),
    path('stock/create/', createStock, name='createSto'),
    path('stock/detail/<int:pk>/', detailStock, name='detailSto'),
    path('stock/list/', listStock, name='listSto'),
    path('stock/detail/<int:pk>/update/', updateStock, name='updateSto'),
    path('stock/detail/<int:pk>/delete/', deleteStock, name='deleteSto'),
]