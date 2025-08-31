from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from upload.models import Upload
from commision_work.models import Commission

from contac_us.models import Contact
from django.core.paginator import Paginator
def home(request):
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
            medium = request.POST.get('medium')
            price = request.POST.get('price')
            image = request.POST.get('image')
            custom = request.POST.get('custom')
       
        data = {'phone': phone1,'email' :email1, 'medium':medium,'price':price,'image':image,'custom':custom}
        commisiondata = Commission(phone=phone1,
email=email1,
medium=medium,
price=price,
image=image,
customization=custom)
        commisiondata.save()
      
    except:
        pass


    return render(request,"home.html",data)

def artworks(request):
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
        sellerart = Upload(title=selltitle,
discription=d,
art=sellerartwork,
price=p)
        sellerart.save()
       
        search = request.POST.get('search')
        if search!=None:
            final = Upload.objects.filter(title__icontains = search)
  

           
        
    except:
        pass
    return render(request, "all_artworks.html", {'artworks': final})

def header(request):
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "header.html", {'artworks': final})
    except:
        pass


def cart(request):
    
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)

        
    sellDescription =''
    artofseller=''
    selltitle=''
    d=''
    p=''
    sellerartwork=''
    sellprice =''
    sellerart=''
    try:
        if request.method=='POST':
            artofseller = request.POST.get('artofseller')
            sellDescription = request.POST.get('selldescription')
            selltitle = request.POST.get('selltitle')
            sellprice = request.POST.get('sellprice')
            d = request.POST.get('d')
            p = request.POST.get('p')
            sellerartwork = request.FILES.get('sellerartwork')
        sellerdata = {"artofseller":artofseller ,"sellprice":sellprice , "sellDescription":sellDescription , "selltitle":selltitle, "d":d, "p":p, "sellerartwork":sellerartwork}
   
        sellerart = Upload(title=selltitle,
discription=d,
art=sellerartwork,
price=p)
        sellerart.save()
    except:
        pass
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "cart.html", {'artworks': final,'sellerdata':sellerdata})
    except:
        pass

      
    

  
   





def learn(request):
    return render(request,"learn.html")


def top(request):

    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "top_artist.html", {'artworks': final})
    except:
        pass



def profile(request):
    return render(request,"profile.html")



# def data(request):
#     phonec = ''
#     emailc = ''
#     statec = ''
#     cityc = ''
#     addressc = ''
#     feedbackc = ''
#     phone1 = ''
#     email1 = ''
#     medium = ''
#     price = ''
#     image = ''
#     custom = '' 
#     selltitle = ''
#     d=''
#     p='' 
#     sellerartwork='' 
#     commisiondata = ''
#     contactdata =''
#     sellerart=''


#     data = {}
#     try:
#         if request.method=='POST':
#             phonec = request.POST.get('phonec')
#             emailc = request.POST.get('emailc')
#             statec = request.POST.get('statec')
#             cityc = request.POST.get('cityc')
#             addressc = request.POST.get('addressc')
#             feedbackc = request.POST.get('feedbackc')
#             phone1 = request.POST.get('phone1')
#             email1 = request.POST.get('email1')
#             medium = request.POST.get('medium')
#             price = request.POST.get('price')
#             image = request.POST.get('image')
#             custom = request.POST.get('custom')
#             selltitle = request.POST.get('selltitle')
#             d = request.POST.get('d')
#             p = request.POST.get('p')
#             sellerartwork = request.FILES.get('sellerartwork')
        
       
      
#         data = {'phone': phone1,'email' :email1, 'medium':medium,'price':price,'image':image,'custom':custom,'phone': phonec,'email' :emailc, 'state':statec,'city':cityc,'address':addressc,'feedback':feedbackc ,  "d":d , "sellerartwork":sellerartwork, "p":p, "title":selltitle}
#         sellerart = Upload(title=selltitle,
# discription=d,
# art=sellerartwork,
# price=p)
#         sellerart.save() 
#         contactdata = Contact(phone=phonec,
# email=emailc,
# state=statec,
# city=cityc,
# address=addressc,
# feedback=feedbackc,
# )
#         contactdata.save()
       
      
       
#         commisiondata = Commission(phone=phone1,
# email=email1,
# medium=medium,
# price=price,
# image=image,
# customization=custom)
#         commisiondata.save()
        
#     except:
#         pass
#     return render(request,"data.html",data )





def data(request):
    phonec = ''
    emailc = ''
    statec = ''
    cityc = ''
    addressc = ''
    feedbackc = ''
    contactdata =''

    
    phone1 = ''
    email1 = ''
    medium = ''
    price = ''
    image = ''
    custom = ''  
    sellprice=''
    sellDescription=''
    artofseller='' 
    selltitle = ''
    d=''
    p='' 
    sellerartwork='' 
    commisiondata = ''

    sellerart=''
    data = {}
    try:
        if request.method=='POST':
            phonec = request.POST.get('phonec')
            emailc = request.POST.get('emailc')
            statec = request.POST.get('statec')
            cityc = request.POST.get('cityc')
            addressc = request.POST.get('addressc')
            feedbackc = request.POST.get('feedbackc')
        
            phone1 = request.POST.get('phone1')
            email1 = request.POST.get('email1')
            medium = request.POST.get('medium')
            price = request.POST.get('price')
            image = request.POST.get('image')
            custom = request.POST.get('custom')
            sellprice = request.POST.get('sellprice')
            artofseller = request.POST.get('artofseller')
            sellDescription = request.POST.get('selldescription')
            selltitle = request.POST.get('selltitle')
            d = request.POST.get('d')
            p = request.POST.get('p')
            sellerartwork = request.POST.get('sellerartwork')
        
       
      
        data = {'phone': phone1,'email' :email1, 'medium':medium,'price':price,'image':image,'custom':custom,'phone': phonec,'email' :emailc, 'state':statec,'city':cityc,'address':addressc,'feedback':feedbackc , "artofseller":artofseller , "sellprice":sellprice ,"sellDescription":sellDescription , "d":d , "sellerartwork":sellerartwork, "p":p, "title":selltitle}
        return render(request,"data.html",data )
        con
    except:
        pass





def contact(request):
    phonec = ''
    emailc = ''
    statec = ''
    cityc = ''
    addressc = ''
    feedbackc = ''
    contactdata =''
    data = {}
    try:
        if request.method=='POST':
            phonec = request.POST.get('phonec')
            emailc = request.POST.get('emailc')
            statec = request.POST.get('statec')
            cityc = request.POST.get('cityc')
            addressc = request.POST.get('addressc')
            feedbackc = request.POST.get('feedbackc')
        
        data = {'phone': phonec,'email' :emailc, 'state':statec,'city':cityc,'address':addressc,'feedback':feedbackc}
        contactdata = Contact(phone=phonec,
email=emailc,
state=statec,
city=cityc,
address=addressc,
feedback=feedbackc,
)
        contactdata.save()
      
    except:
        pass

    return render(request, "contact.html",data)



def purchase(request):
    return render(request,"purchase.html")


