from django.shortcuts import render,redirect
import requests
from .import models
# Create your views here.


def homepage(req):
    carttable = models.cart.objects.all().values()
    return render(req, 'index.html', context={'Orders': carttable})


def dataChange(req):
    carttable = models.cart.objects.all().values()
    return render(req, 'data.html', context={'Orders': carttable})

def ecom(req):
    response = requests.get('https://dummyjson.com/products', params={"limit": 20})
    data = response.json()
    print(data)
    brandList = []
    # for i in data['products']:
    #     if i['price'] == 9.99:
    #         priceList.append(i)
    # print(priceList)
    return render(req, 'ecom.html', context={"productList": data['products'], 'brandproductList': brandList})


def deleteOrder(req, id):
    order = models.cart.objects.get(id=id)
    order.delete()
    # order.name = req.POST.get('name')
    # order.size = req.POST.get('name')
    # order.brand = req.POST.get('name')
    # order.contact = req.POST.get('name')
    # order.price = req.POST.get('name')
    # order.save()
    return redirect('/home')

def alterOrder(req,id):
    if req.method=="POST":
        order=models.cart.objects.get(id=id)
        order.name=req.POST['productName']
        order.save()
        return redirect('/data')
    else:
        print(req.method)
        order=models.cart.objects.get(id=id)
        return render(req,'alter.html',context={"data":order})
