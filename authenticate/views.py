from random import randint
from authenticate.forms import TeacherForm,StudentForm,UserProfileChange,StudentMedia
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'authenticate/index.html')

def teacher_register(request):
    flag = False
    if(request.method == 'POST'):
        Teacherform = TeacherForm(request.POST)
        if(Teacherform.is_valid()):
            new_Teacherform = Teacherform.save(commit = False)
            # id = request.POST['id']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            password = request.POST['password']
            email = request.POST['email']
            new_Teacherform.set_password(new_Teacherform.password)

            new_Teacherform.save()
            flag = True

    else:
        Teacherform = TeacherForm()

    dic = {
        'Teacherform':Teacherform,
        'flag':flag,
    } 
    return render(request,'authenticate/tea_register.html',context=dic)   

def student_register(request):
    flag = False
    if(request.method == 'POST'):
        Studentform = StudentForm(request.POST)
        # stu_media = StudentMedia(request.POST)
        if(Studentform.is_valid()):
            new_Studentform = Studentform.save(commit = False)
            # id = request.POST['id']
            # fname = request.POST['first_name']
            # lname = request.POST['last_name']
            # password = request.POST['password']
            email = request.POST['email']
            new_Studentform.set_password(new_Studentform.password)
            new_Studentform.save()

            # stu_info_media = stu_media.save(commit=False)
            # stu_info_media.user = new_Studentform
            
            # if 'profile_pic' in request.FILES:
            #     stu_info_media.profile_pic =request.FILES['profile_pic']
            # stu_info_media.save()
            flag = True
            return HttpResponseRedirect('/web/portal/')

    else:
        Studentform = StudentForm()
        stu_info_media =StudentMedia()

    dic = {
        'Studentform':Studentform,
        # 'stu_info_media':stu_info_media,
        'flag':flag,
    } 
    return render(request,'authenticate/stu_register.html',context=dic)   

def teacher_login(request):
    tea_info = AuthenticationForm()
    if(request.method =='POST'):
        tea_info = AuthenticationForm(data=request.POST)
        if(tea_info.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if(user is not None):
                login(request,user)
                return HttpResponseRedirect('/web/portal/')

    return render(request,'authenticate/tea_login.html',{'tea_info':tea_info})

def student_login(request):
    stu_info = AuthenticationForm()
    if(request.method =='POST'):
        stu_info = AuthenticationForm(data=request.POST)
        if(stu_info.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if(user is not None):
                login(request,user)
                return HttpResponseRedirect('/web/stu_portal/')
                
    return render(request,'authenticate/stu_login.html',{'stu_info':stu_info})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/index/')

@login_required
def user_profile(request):
    return render(request,'authenticate/stu_profile.html')

@login_required
def admin_profile(request):
    return render(request,'authenticate/tea_profile.html')

@login_required
def change_user(request):
    form = UserProfileChange(instance=request.user)
    if(request.method == 'POST'):
        form = UserProfileChange(data=request.POST,instance=request.user)
        if(form.is_valid()):
            form.save()
            form = UserProfileChange(instance=request.user)
            return HttpResponseRedirect('/user/tea_profile/')
    return render(request,'authenticate/chng_stu_prfle.html',{'form':form})


# def change_pass(request):
#     flag = False
#     form= PasswordChangeForm(user=request.user)
#     if(request.method == 'POST'):
#         form = PasswordChangeForm(data=request.POST,user=request.user)
#         if(form.is_valid()):
#             update_session_auth_hash(request,form.user)
#             flag = True
#     dic = {
#         'flag':flag,
#         'form':form,
#     }
#     return render(request,'authenticate/change_password.html',context=dic)





