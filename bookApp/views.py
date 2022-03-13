from django.shortcuts import redirect, render
from bookApp.models import Book 

def book_home(request):
    if(request.method == 'GET'):
        return render(request,'bookApp/index.html')

    if(request.method == 'POST'):

        name = request.POST['name']
        price = request.POST['price']        
        qty = int(request.POST['qty'])      
        author = request.POST['author']

        if (qty == 0):
            dic={
                'msg':'At least 1 Book required'

            }
            return render(request,'bookApp/index.html',context=dic)
        else:
            book_info = Book(name=name, price=price, qty=qty, au_name=author)
            book_info.save()

            dic = {
                'msg':'Data Inserted'
            }

        return render(request,'bookApp/index.html',context=dic)

def book_display(request):

    book_data = Book.objects.raw('select * from bookApp_book')
    return render(request,'bookApp/display.html',{'book_data':book_data})

def book_update(request,id):
    if(request.method == 'POST'):
        id = request.POST['id']
        name = request.POST['name']
        price = request.POST['price']
        qty = request.POST['qty']
        au_name = request.POST['author']

        Book.objects.filter(id=id).update(id=id,name=name,price=price,qty=qty,au_name=au_name)
        return redirect('book_display')
    else:
        book_in = Book.objects.get(id=id)
        return render(request,'bookApp/update_book.html',{'book_in':book_in})

def book_delete(request,id):

    book_data = Book.objects.get(id=id)
    book_data.delete()
    return redirect('book_display')
    


def find_book(request):
    if(request.method == 'GET'):
        return render(request,'bookApp/find_book.html')

    if(request.method == 'POST'):

        find = request.POST['find']
        checkBook = Book.objects.raw('select * from bookApp_book where au_name = "'+ find +'" or name = "'+ find +'"')
        if(len(checkBook)==0):
            msg='record not found'
            print(len(checkBook))

            return render(request,'bookApp/find_book.html',{'msg':msg})
        else:
            print(len(checkBook))
            return render(request,'bookApp/find_display.html',{'checkBook':checkBook})

        
def srch_book(request):
    if(request.method == 'GET'):
        book_obj = Book.objects.all()
        return render(request,'bookApp/book_srch.html',{'book_obj':book_obj})
        
    if(request.method == 'POST'):
        id = request.POST['id']
        name = request.POST['name']
        book_obj = Book.objects.all()
        for book in Book.objects.filter(id=id,name=name):
            print(book.price)
            print(book.qty)
            print(book.au_name)
            return render(request,'bookApp/book_srch.html',{'book':book,'book_obj':book_obj})
        else:
            msg='Record does not found'
            return render(request,'bookApp/book_srch.html',{'msg':msg,'book_obj':book_obj})
       
            
    
        



        

