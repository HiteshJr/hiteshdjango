from django.shortcuts import render, redirect
import requests
import json
from . import models

# Create your views here.
userID = 1

def homepage(req):
    cartTable = models.cart.objects.all().values()
    return render(req,'index.html',context={'table':cartTable})

def dataChange(req):
    cartTable = models.cart.objects.all().values()
    return render(req,'data.html',context={'table':cartTable})
    
def ecom(req):
    response = requests.get('https://dummyjson.com/products',params={"limit":20})
    data = response.json()
    print(data)
    #   brandList = []
    # for i in data['products']:
    #     if i['brand'] == 'Essence':
    #         brandList.append(i)
    return render(req,'ecom.html',context={"productList":data['products']})

def deleteOrder(req,id):
    order = models.cart.objects.get(id=id)
    order.delete()
    return redirect('/home')

def alterOrder(req,id):
    if req.method == "POST":
        order = models.cart.objects.get(id=id)
        order.name = req.POST['productName']
        order.save()
        return redirect('/data')
    else:
        print(req.method)
        order = models.cart.objects.get(id=id)
        return render(req,"alter.html",context={"data":order})
    
def buyProduct(req,id):
    response = requests.get(f'https://dummyjson.com/products/{id}')
    data = response.json()
    print(data)
    return render(req,"buy.html",context={"data":data})

def addTocart(req,id):
   user = models.users.objects.get(id = userID)
   usercart = json.loads(user.cart)
   usercart.append(id)
   user.cart = usercart
   user.save()  
   print(usercart)
   return redirect(f"/buy/{id}?addedtocart=true")

def removeFromcart(req,id):
   user = models.users.objects.get(id = userID)
   usercart = json.loads(user.cart)
   usercart.remove(id)
   user.cart = usercart
   user.save()  
   print(usercart)
   return redirect(f"/cart?removefromcart=true")

def cartpage(req):
   user = models.users.objects.get(id = userID)
   usercart = json.loads(user.cart)
   cartItem= []
   for i in usercart:
        response = requests.get(f'https://dummyjson.com/products/{i}')
        data = response.json()
        cartItem.append(data)
   return render(req,'cart.html',context={"cartitem":cartItem})