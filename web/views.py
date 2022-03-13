from django.http.response import HttpResponseRedirect
from web.models import Stu_Class, StudentDetails,StudentResult
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from random import randint





def main(request):
    if (request.method == 'GET'):
        return render(request,'web/main.html')

@login_required
def portal(request):
    if (request.method == 'GET'):
        return render(request,'web/portal.html')

    # if (request.method == 'POST'): 
    #     return render(request,'web/info.html') 

# def stu_info(request):
#     if (request.method == 'GET'):
#         return render(request,'web/stu_info.html') 
    
#     if (request.method == 'POST'):
#         id = request.POST['id']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         mobile = request.POST['mobile']
#         password = request.POST['password']

#         tea_obj = Stu_register(id=id,fname=fname,lname=lname,email=email,mobile=mobile,password=password)
#         tea_obj.save()
#         return render(request,'web/success.html') 

# def tea_info(request):
#     if (request.method == 'GET'):
#         return render(request,'web/tea_info.html') 
    
#     if (request.method == 'POST'):
#         id = request.POST['id']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         mobile = request.POST['mobile']
#         password = request.POST['password']

#         tea_obj = Tea_register(id=id,fname=fname,lname=lname,email=email,mobile=mobile,password=password)
#         tea_obj.save()
#         return render(request,'web/success.html') 
@login_required
def student_details(request):
    if (request.method == 'GET'):
        stu_obj = Stu_Class.objects.all()
        return render(request,'web/student.html',{'stu_obj':stu_obj})

    if (request.method == 'POST'):
        id = (request.POST['id'])
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']

        parent = request.POST['parent']
        standard = request.POST['standard']
        address= request.POST['address']
        email= request.POST['email']
        phone= request.POST['phone']
        p_phone= request.POST['p_phone']
        

        # request.session['id']=id
        stu_obj = Stu_Class.objects.all()
        checkStudent = StudentDetails.objects.raw('select * from web_studentdetails where id ="'+ id+'"' )
        if(len(checkStudent)>0):
            dic={
                'msg':'This ID already exists, try a new id',
                'stu_obj':stu_obj,
            }
            return render(request,'web/student.html',context=dic)
        else:
            stu_obj = Stu_Class.objects.all()
            
            student = StudentDetails(id=id,first_name=fname,last_name=lname,date_of_birth=dob,guardian_name=parent,standard_id=standard,address=address,email=email,mobile=phone,guardian_mobile=p_phone)
           
            student.save()
          
            # stu_obj = Stu_Class.objects.all()

        # return render(request,'web/student.html',{'stu_obj':stu_obj,'student':student})
        return HttpResponseRedirect('/user/stu_register/')

@login_required
def display_student(request):
    student_info = StudentDetails.objects.raw('select * from web_studentdetails')
    return render(request,'web/display_student.html',{'student_info':student_info})

@login_required
def update_student(request,id):
    if(request.method == 'POST'):
        # id = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        parent = request.POST['parent']
        standard = request.POST['standard']
        address= request.POST['address']
        email= request.POST['email']
        phone= request.POST['phone']
        p_phone= request.POST['p_phone']

        StudentDetails.objects.filter(id=id).update(first_name=fname,last_name=lname,date_of_birth=dob,guardian_name=parent,standard=standard,address=address,email=email,mobile=phone,guardian_mobile=p_phone)
        return redirect('display')
    else:
        stud_data = StudentDetails.objects.get(id=id)
        return render(request,'web/update_student.html',{'stud_data':stud_data})

@login_required
def delete_student(request,id):
    stud_info = StudentDetails.objects.get(id=id)
    stud_info.delete()
    return redirect('display')

@login_required
def student_result(request):
    if (request.method == 'GET'):
        return render(request,'web/stu_result.html')

    if (request.method == 'POST'):
        roll = (request.POST['roll'])
        name = request.POST['name']
        eng = int(request.POST['english'])
        math = int(request.POST['math'])

        sc = int(request.POST['science'])
        hist = int(request.POST['history'])
        geo= int(request.POST['geography'])

        total =( eng + math + sc + hist + geo )
        percent = ( total / 5 ) 
        if(percent >= 90 ):
            grade ='O'
        elif(percent >= 80 and percent < 90):
            grade ='E'
        elif(percent >= 70 and percent < 80):
            grade ='A'
        elif(percent >= 60 and percent < 70):
            grade ='B'
        elif(percent >= 50 and percent < 60):
            grade ='C'
        elif(percent >= 33 and percent < 50):
            grade ='D'
        else:
            grade ='F'

        check_res = StudentResult.objects.raw('select * from web_studentresult where roll ="'+roll+'"')
        if(len(check_res)>0):
            msg='This roll number already exist.Please enter a unique roll number'
            return render(request,'web/stu_result.html',{'msg':msg})
        else:
            stud_res = StudentResult(roll=roll,s_name=name,english=eng,math=math,science=sc,history=hist,geography=geo,total=total,percent=percent,grade=grade)

            stud_res.save()
            # msg='record saved'
        dic ={
            'stud_res':stud_res
        }

        return render(request,'web/portal.html',{'stud_res':stud_res})

@login_required
def display_result(request):
    get_result = StudentResult.objects.raw('select * from web_studentresult')
    return render(request,'web/display_result.html',{'get_result':get_result})

@login_required
def update_result(request,roll):
    if (request.method == 'POST'):
        roll = (request.POST['roll'])
        name = request.POST['name']
        eng = int(request.POST['english'])
        math = int(request.POST['math'])

        sc = int(request.POST['science'])
        hist = int(request.POST['history'])
        geo= int(request.POST['geography'])

        total = (eng + math + sc + hist + geo)

        percent = (total / 5)
        if(percent >= 90 ):
            grade ='O'
        elif(percent >= 80 and percent < 90):
            grade ='E'
        elif(percent >= 70 and percent < 80):
            grade ='A'
        elif(percent >= 60 and percent < 70):
            grade ='B'
        elif(percent >= 50 and percent < 60):
            grade ='C'
        elif(percent >= 33 and percent < 50):
            grade ='D'
        else:
            grade ='F'
        
        StudentResult.objects.filter(roll=roll).update(s_name=name,english=eng,math=math,science=sc,history=hist,geography=geo,total=total,percent=percent,grade=grade)
        return redirect('display_result')

    else:
        res_info = StudentResult.objects.get(roll=roll)
        return render(request,'web/update_result.html',{'res_info':res_info})

@login_required
def delete_result(request,roll):
    res_data = StudentResult.objects.get(roll=roll)
    res_data.delete()
    return redirect('display_result')

@login_required
def result(request,id):

    result_data = StudentDetails.objects.get(id=id)
    return render(request,'web/stu_result',{'result_data':result_data})

@login_required
def student_portal(request):
    return render(request,'web/student_portal.html')

@login_required
def search_result(request):
    if(request.method == 'GET'):
        return render(request,'web/search_result.html')
    if(request.method == 'POST'):
        find = (request.POST['find'])
        check_result = StudentResult.objects.raw('select * from web_studentresult where roll ="'+ find +'"')
        if(len(check_result)<1):
            msg="please enter a valid id"
            return render(request,'web/search_result.html',{'msg':msg})
        else:
            return render(request,'web/dis_stu_res.html',{'check_result':check_result})

@login_required
def search_student(request):
    if(request.method == 'GET'):
        return render(request,'web/search_student.html')
    if(request.method == 'POST'):
        srch = (request.POST['fname'])
        srch_result = StudentDetails.objects.raw('select * from web_studentdetails where first_name ="'+ srch +'" or id="'+ srch +'" ')
        if(len(srch_result)<1):
            msg="Student Not found"
            return render(request,'web/search_student.html',{'msg':msg})
        else:
            return render(request,'web/stu_src.html',{'srch_result':srch_result})

def graph_chart(request):
    labels = []
    data = []
    queryset = StudentResult.objects.order_by('english')
    for query in queryset:
        labels.append(StudentResult.s_name)
        data.append(StudentResult.english)
    return render(request,'web/graph.html',{'labels':labels,'data':data})

def chart(request):
    labels = []
    data = []
    query = StudentResult.objects.all()
    for que in query:
        labels.append(StudentResult.english)
        data.append(StudentResult.math)
    dic ={
            'labels':labels,
            'data':data,
            'query':query,
        }
    return render(request,'web/chart_graph.html',context=dic)


def standard(request):
    if(request.method == 'GET'):
        return render(request,'web/student_standard.html')

    if(request.method == 'POST'):
        standard = request.POST['standard']

        stan = Stu_Class(standard=standard)
        stan.save()

        return render(request,'web/student_standard.html',{'stan':stan})

