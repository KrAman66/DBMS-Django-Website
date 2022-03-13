from django.shortcuts import render

def start(request):

    if(request.method == 'GET'):
        return render(request,'startup2.html')


def extend(request):
    
    if(request.method == 'GET'):
        return render(request,'extend.html')
