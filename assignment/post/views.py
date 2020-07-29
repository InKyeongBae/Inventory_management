import logging
from django.shortcuts import render, redirect, reverse
from .models import Stock,Account
# Create your views here.

def home(request) :
    return render(request,'post/list_stock.html')

def createAccount(request) :
    if request.method == "GET":
        return render(request,'post/create_account.html',context={})

    name=request.POST['name']
    call=request.POST['call']
    address=request.POST['address']
    account=Account.objects.create(name=name, call=call, address=address)
    pk=account.id
    url = reverse('post:detailAcc', kwargs={'pk':pk})
    return redirect(to=url)

def detailAccount(request, pk):
    account = Account.objects.get(id=pk)
    context = {
        'account' : account
    }
    return render(request,'post/detail_account.html',context=context)

def listAccount(request):
    queryset = Account.objects.all()
    context = {
        'accounts' : queryset,
    }
    return render(request,'post/list_account.html',context=context)

def deleteAccount(request,pk):
    account=Account.objects.get(id=pk)
    account.delete()

    url = reverse('post:listAcc')
    return redirect(to=url)

def updateAccount(request, pk):
    account=Account.objects.get(id=pk)

    if request.method =='GET':
        context = {
            'account':account
        }
        return render(request,'post/update_account.html',context=context)

    name=request.POST['name']
    call=request.POST['call']
    address=request.POST['address']
    #DB에 바꿀 내용들
    account.name=name
    account.call=call
    account.address=address
    account.save()

    url = reverse('post:detailAcc', kwargs={'pk': pk})
    return redirect(to=url)


def createStock(request) :
    if request.method == "GET":
        return render(request,'post/create_stock.html',context={})

    title=request.POST['title']
    image=request.POST['image']
    content=request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    stock=Stock.objects.create(title=title, image=image, content=content, price=price, amount=amount)
    pk=stock.id
    url = reverse('post:detailSto', kwargs={'pk':pk})
    return redirect(to=url)

def detailStock(request, pk):
    stock = Stock.objects.get(id=pk)
    context = {
        'stock' : stock
    }
    return render(request,'post/detail_stock.html',context=context)

def listStock(request):
    queryset = Stock.objects.all()
    context = {
        'stocks' : queryset,
    }
    return render(request,'post/list_stock.html',context=context)

def deleteStock(request,pk):
    stock=Stock.objects.get(id=pk)
    stock.delete()

    url = reverse('post:listSto')
    return redirect(to=url)

def updateStock(request, pk):
    stock=Stock.objects.get(id=pk)

    if request.method =='GET':
        context = {
            'stock':stock
        }
        return render(request,'post/update_stock.html',context=context)

    title=request.POST['title']
    image=request.POST['image']
    content=request.POST['content']
    price = request.POST['price']
    amount = request.POST['amount']
    #DB에 바꿀 내용들
    stock.title=title
    stock.image=image
    stock.content=content
    stock.price=price
    stock.amount=amount
    stock.save()

    url = reverse('post:detailSto', kwargs={'pk': pk})
    return redirect(to=url)