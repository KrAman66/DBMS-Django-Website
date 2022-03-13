from django.shortcuts import render, redirect
from newapp.models import Add, Book
from django.http import HttpResponse, response,HttpResponseRedirect


def home(request):

    if(request.method == 'GET'):
        return render(request,'newapp/intro.html')

    if(request.method == 'POST'):
        name = request.POST['name']
        price = request.POST['price']

        book = Book.objects.raw('select * from newapp_book')
        book_info = Book(name=name,price=price)
        book_info.save()

        dic ={
            'name':name,
            'price':price,
            'msg':'Succesfully insert'
            }


        return render(request,'newapp/intro.html',context=dic)


def display(request):
    
    book = Book.objects.raw('select * from newapp_book')
    return render(request,'newapp/display.html',{'book':book})

def update(request,id):

    update_book = Book.objects.get(id=id)
    return render(request,'newapp/update.html',{'a':update_book})


def addition(request):
    if (request.method=='GET'):
        return render(request,'newapp/sum.html')

    if(request.method == 'POST'):
        # name = (request.POST["val1"]
        value1 = int(request.POST["val1"])
        value2 = int(request.POST["val2"])

        value3 = value1 + value2
        # obj = Add.objects.raw('select * from newapp_add ')
        # obj = Add(name=name,num1=value1,num2=value2,num3=value3)
        # obj.save()
       
        # request.session['v1'] = value1
        # request.session['v2'] = value2

        return render(request,'newapp/sum.html',{'v1':value1,
        'v2':value2,
        'v3':value3})
        

def result(request):
    value1 = request.session.get('v1')
    value2 = request.session.get('v2')
    value3 = value1 + value2
    request.session.flush()
    return render(request,'newapp/result.html',{'value1':value1,
        'value2':value2,
        'value3':value3,})

        
   
    

