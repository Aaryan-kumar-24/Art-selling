from django.shortcuts import render,redirect
from django.http import HttpResponse
from upload.models import Upload
from learn.models import Learn
from commision_work.models import Commission
from contact.models import Contact
from artist.models import Artist
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect


def login_signup(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "signup":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            role = request.POST.get('role')

            if password != confirm_password:
                return HttpResponse("Password and Confirm Password do not match")

            if User.objects.filter(username=name).exists():
                return HttpResponse("Username already exists")

            new_user = User.objects.create_superuser(username=name, email=email, password=password)
            new_user.first_name = phone
            new_user.last_name = role
            new_user.save()
            return redirect('login_signup')

        elif form_type == "login":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                return HttpResponse("Invalid username or password")

    return render(request, "login_signup.html")



def logout_page(request):   
    logout(request)
    return redirect('logout_page')


@login_required(login_url='login_signup')
def home(request):
    commisiondatas = Commission.objects.all()
  
    paginator = Paginator(commisiondatas,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)

    phone1 = ''
    email1 = ''
    medium = ''
    price = ''
    image = ''
    custom = ''
    commisiondata = ''
    data = {}
    try:
        if request.method=='POST':
            phone1 = request.POST.get('phone1')
            email1 = request.POST.get('email1')
            artist = request.POST.get('artist')
            medium = request.POST.get('medium')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            custom = request.POST.get('custom')
       
        data = {'phone': phone1,'email' :email1, 'artist':artist, 'medium':medium,'price':price,'image':image,'custom':custom}
        commisiondata = Commission(phone=phone1,
email=email1,
artist=artist,
medium=medium,
price=price,
image=image,
customization=custom)
        commisiondata.save()
        
    except:
        pass
    artists=Artist.objects.all()
    return render(request,"home.html",{"data":data , "artworks":final , "artists":artists})


@login_required(login_url='login_signup')
def artworks(request):
    myupload = Upload.objects.all()
    paginator = Paginator(myupload,12)
   
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
      
    try:
        if request.method=='POST': 
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)      
    except:
        pass

    return render(request, "all_artworks.html", {'artworks': final})


@login_required(login_url='login_signup')
def header(request):
    user = request.user
    phone = user.first_name    
    role = user.last_name 
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
    except:
        pass
    
    return render(request, "header.html", {'artworks': final,'user': user,'phone':phone,'role':role})


@login_required(login_url='login_signup')
def cart(request):
    user = request.user
    role = user.last_name
    myupload = Upload.objects.all() 
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)

    selltitle=''
    d=''
    p=''
    sellerartwork=''
    sellerart=''
    try:
        if request.method=='POST':
            selltitle = request.POST.get('selltitle')
            d = request.POST.get('d')
            p = request.POST.get('p')
            sellerartwork = request.FILES.get('sellerartwork')

            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  
            sellerart=Upload(title=selltitle,
discription=d,
art=sellerartwork,
price=p)    
            sellerart.save()
        sellerdata = { "selltitle":selltitle, "d":d, "p":p, "sellerartwork":sellerartwork}
   
        final =Upload.objects.filter(user=request.user)
    except:
        pass           
    return render(request, "cart.html", {'artworks': final,'sellerdata':sellerdata})



@login_required(login_url='login_signup')
def learn(request):
    learndata = Learn.objects.all()
    return render(request,"learn.html" , {"learn":learndata})


@login_required(login_url='login_signup')
def profile(request):
    user = request.user
    role = user.last_name
    if request.method == 'POST':
        form_type = request.POST.get("form_type")
        if form_type == "artist":
            artistpic =request.FILES.get('artistpic')
            artistname =request.POST.get('artistname')
    

            artist=Artist(artistpic=artistpic,
artistname=artistname,)    
            artist.save()
            redirect('profile')


        elif form_type == "artwork":
            selltitle = request.POST.get('selltitle')
            d = request.POST.get('d')
            p = request.POST.get('p')
            sellerartwork = request.FILES.get('sellerartwork')

            sellerart=Upload(title=selltitle,
discription=d,
art=sellerartwork,
price=p)    
            sellerart.save()
            redirect('profile')
        
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                Commission.objects.get(id=delete_id).delete()
            except Commission.DoesNotExist:
                pass
        return redirect('profile')

    if role == 'seller':
        buyers = Commission.objects.filter(artist=user.username)  
    else:
        buyers = Commission.objects.none()  
    
    return render(request, 'profile.html', {'buyers': buyers, 'user': user, 'role': role})


@login_required(login_url='login_signup')
def contact(request):
    if request.method == 'POST':
        phonenumber = request.POST.get('phonenumber')
        emailid = request.POST.get('emailid')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        review = request.POST.get('review')

        Contact.objects.create(
            phonenumber=phonenumber,
            emailid=emailid,
            state=state,
            city=city,
            address=address,
            review=review
        )
        return redirect('contact')  
    
    return render(request, "contact.html")

@login_required(login_url='login_signup')
def purchase(request):
    return render(request,"purchase.html")

@login_required(login_url='login_signup')
def index(request):
    return render(request,"index.html")