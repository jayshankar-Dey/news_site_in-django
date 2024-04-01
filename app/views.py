from django.shortcuts import redirect, render
from . models import Cat,Post,register,total_views
# Create your views here.
def home(request):
    all = Post.objects.order_by('-id').all()[4:8]
    al = Cat.objects.all()
    alls = Post.objects.order_by('-id').all()[0:4]
    
    return render(request,"home.html",{'all':all,'cat':al,'alls':alls})
# show data................
def show(request,id):
    all = Post.objects.filter(id=id)
    al = Cat.objects.all()
    uid = request.session.get("id")
    if uid:
     find = total_views.objects.filter(pid=id,uid=request.session.get("id"))
     if find:
        count = total_views.objects.filter(pid=5).count()
       
        return render(request,"show.html",{'all':all,'cat':al,'count':count})
     else:
       uid = request.session.get("id")
       print(request.session.get("id"))
       total_views.objects.create(uid=uid,pid=id)
      
       return render(request,"show.html",{'all':all,'cat':al})
    else:
       return redirect("log")
    

def log(request):
    return render(request,"login.html")
def reg(request):
    return render(request,"register.html")
#register hear.......................................
def registers(request):
    if request.method == 'POST':
     email = request.POST.get('email')
     password = request.POST.get('password')
     repassword = request.POST.get('Repassword')
     
    if password == repassword and email != "":
      find = register.objects.filter(email=email)
      if find:
         request.session['error'] = "Email alrady exist"
         request.session.set_expiry(5)
         return redirect('reg')
      else:
         request.session['success'] = "Register succesful"
         request.session.set_expiry(5)
         register.objects.create(email=email,password=password)
         return redirect('log')
    else:
        request.session['error'] = "Password not match"
        request.session.set_expiry(5)
        # return render(request,"register.html",{'msg':'error'})
        return redirect('reg')
    
def login(request):
    if request.method == 'POST':
     email = request.POST.get('email')
     password = request.POST.get('password')
     find = register.objects.filter(email=email,password=password)
     if find:
        for find in find:
           id = find.id
           request.session['id'] = id
        return redirect('home')
     else:
        return redirect('log')

def filter(request,fid):
    data = Post.objects.filter(pcat=fid)
    al = Cat.objects.all()
    return render(request,"filter.html",{'all':data,'cat':al})


   
    
        
         
         
     