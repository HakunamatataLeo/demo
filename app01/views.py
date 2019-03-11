from django.shortcuts import render
from app01 import models
# from django.db import  models
# Create your views here.

def userInfo(req):
    info_list=[]
    if req.method=="POST":
        username=req.POST.get("username",None)
        sex=req.POST.get("sex",None)
        email=req.POST.get("email",None)

        info={"username":username,"sex":sex,"email":email}
        info_list.append(info)

    return render(req,"userInfor.html",{"info_list":info_list})



# Create your views here.


def userInforx(req):
    
    if req.method=="POST":
        u=req.POST.get("username",None)
        s=req.POST.get("sex",None)
        e=req.POST.get("email",None)

       #---------表中插入数据方式一
        # info={"username":u,"sex":e,"email":e}
        # models.UserInfor2.objects.create(**info)

       # ---------表中插入数据方式二
        models.UserInfor2.objects.create(
            username=u,
            sex=s,
            email=e
        )

        info_list= models.UserInfor2.objects.all()

        return render(req,"userInfor2.html",{"info_list":info_list})

    return render(req,"userInfor2.html")