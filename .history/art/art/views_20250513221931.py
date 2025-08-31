from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from upload.models import Upload
from django.core.paginator import Paginator
def home(request):
    phone1 = ''
    email1 = ''
    medium = ''
    price = ''
    image = ''
    custom = ''
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
      
      
    except:
        pass


    return render(request,"home.html",data)

def artworks(request):
    myupload = Upload.objects.all()
  
    paginator = Paginator(myupload,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "all_artworks.html", {'artworks': final})
    except:
        pass


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
    i=''
    sellprice =''
    try:
        if request.method=='POST':
            artofseller = request.POST.get('artofseller')
            sellDescription = request.POST.get('selldescription')
            selltitle = request.POST.get('selltitle')
            sellprice = request.POST.get('sellprice')
            d = request.POST.get('d')
            p = request.POST.get('p')
            i = request.POST.get('i')
        sellerdata = {"artofseller":artofseller ,"sellprice":sellprice , "sellDescription":sellDescription , "selltitle":selltitle, "d":d, "p":p, "i":i}
    except:
        pass
    
    try:
        if request.method == 'POST':
            search = request.POST.get('search')
            if search!=None:
                final = Upload.objects.filter(title__icontains = search)
  

           
        return render(request, "all_artworks.html", {'artworks': final,'se'})
    except:
        pass

      
    

  
   





def learn(request):
    return render(request,"learn.html")


def top(request):

    artworks = [
    {
        'title': 'Budha',
        'description': 'A calm and spiritual charcoal depiction of Lord Buddha, reflecting peace and wisdom.',
        'price': 2499,
        'image_url': '/static/budha.jpg'
    },
    {
        'title': 'Horse',
        'description': 'An energetic charcoal sketch of a running horse, symbolizing strength and freedom.',
        'price': 2199,
        'image_url': '/static/horse.jpg'
    },
    {
        'title': 'Adiyogi',
        'description': 'A divine representation of Adiyogi, carved in bold strokes capturing cosmic energy.',
        'price': 2099,
        'image_url': '/static/adiyogi.jpg'
    },
    {
        'title': 'Deer',
        'description': 'A graceful deer captured in monochrome, evoking nature’s gentleness and elegance.',
        'price': 1599,
        'image_url': '/static/deer.jpg'
    },
    {
        'title': 'Baby',
        'description': 'A touching charcoal sketch capturing the pure emotion and innocence of a sleeping infant.',
        'price': 2299,
        'image_url': '/static/baby.jpg'
    },
    {
        'title': 'Baby Leg',
        'description': 'A minimalist charcoal artwork showing the tiny feet of a baby, symbolizing new beginnings and life.',
        'price': 1899,
        'image_url': '/static/baby_leg.jpg'
    },
    {
        'title': 'Eagle',
        'description': 'An intense charcoal portrait of an eagle, reflecting vision, strength, and untamed wilderness.',
        'price': 1999,
        'image_url': '/static/eagel.jpg'
    },
    {
        'title': 'Elephant',
        'description': 'A noble charcoal rendering of an elephant, showcasing power, wisdom, and nature’s grandeur.',
        'price': 1899,
        'image_url': '/static/elephant.jpg'
    },
    {
        'title': 'Shivaji',
        'description': 'Charcoal tribute to Shivaji Maharaj, radiating courage, leadership, and historical pride.',
        'price': 2199,
        'image_url': '/static/shivaji.jpg'
    },
    {
        'title': 'Hanuman',
        'description': 'Powerful charcoal art of Lord Hanuman, embodying loyalty, divine strength, and unwavering faith.',
        'price': 1999,
        'image_url': '/static/hanuman.jpg'
    },
    {
        'title': 'Krishna',
        'description': 'Charcoal sketch of Lord Krishna playing the flute, radiating divine charm and eternal serenity.',
        'price': 2099,
        'image_url': '/static/krishna.jpg'
    },
    {
        'title': 'Lady',
        'description': 'A refined charcoal portrait of a woman, expressing beauty, dignity, and silent confidence.',
        'price': 1899,
        'image_url': '/static/lady.jpg'
    },
    {
        'title': 'Arjun',
        'description': 'Charcoal portrait of warrior Arjun in deep Surrender, symbolizing strength, purpose, and ancient valor.',
        'price': 2399,
        'image_url': '/static/arjun.jpg'
    },
    {
        'title': 'Old Man',
        'description': 'A detailed charcoal sketch of an old man\'s face, portraying a lifetime of wisdom and hardship.',
        'price': 1999,
        'image_url': '/static/oldman.jpg'
    },
    {
        'title': 'Panchmukhi Hanuman',
        'description': 'Charcoal rendering of Panchmukhi Hanuman, capturing divine energy, protection, and intense spiritual presence.',
        'price': 2599,
        'image_url': '/static/panchmukhi.jpg'
    },
    {
        'title': 'Rhino',
        'description': 'A bold and rugged charcoal drawing of a rhinoceros, emphasizing power, resilience, and raw nature.',
        'price': 1899,
        'image_url': '/static/rhino.jpg'
    },
    {
        'title': 'Brain',
        'description': 'A conceptual charcoal artwork illustrating the brain’s complexity, intelligence, and the mystery of thought.',
        'price': 1799,
        'image_url': '/static/brain.jpg'
    },
    {
        'title': 'Skull',
        'description': 'Haunting charcoal silhouette of a ghostly figure, invoking mystery, emotion, and surreal darkness.',
        'price': 1999,
        'image_url': '/static/ghost.jpg'
    },
    {
        'title': 'Shiv',
        'description': 'A divine portrayal of Lord Shiva in charcoal, channeling calmness, power, and spiritual balance.',
        'price': 2299,
        'image_url': '/static/shiv.jpg'
    },
    {
        'title': 'Stone Chariot',
        'description': 'Charcoal illustration of the iconic stone chariot from Hampi, reflecting historical grandeur and Indian craftsmanship.',
        'price': 2199,
        'image_url': '/static/stonechariot.jpg'
    }
]
      
    paginator = Paginator(artworks,8)
    page_number = request.GET.get('page')
    final = paginator.get_page(page_number)
     
    return render(request,"top_artist.html",{'artworks': final})




def profile(request):
    return render(request,"profile.html")


def data(request):
    phone = ''
    email = ''
    state = ''
    city = ''
    address = ''
    feedback = ''
    phone1 = ''
    email1 = ''
    medium = ''
    price = ''
    image = ''
    custom = ''  
    sellprice=''
    sellDescription=''
    selltitle = ''
    artofseller='' 
    d=''
    p='' 
    i='' 
    data = {}
    try:
        if request.method=='POST':
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            state = request.POST.get('state')
            city = request.POST.get('city')
            address = request.POST.get('address')
            feedback = request.POST.get('feedback')
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
            i = request.POST.get('i')
        
       
      
        data = {'phone': phone1,'email' :email1, 'medium':medium,'price':price,'image':image,'custom':custom,'phone': phone,'email' :email, 'state':state,'city':city,'address':address,'feedback':feedback , "artofseller":artofseller , "sellprice":sellprice ,"sellDescription":sellDescription , "d":d , "i":i, "p":p, "title":selltitle}
        return render(request,"data.html",data )
    except:
        pass

def contact(request):
    phone = ''
    email = ''
    state = ''
    city = ''
    address = ''
    feedback = ''
    data = {}
    try:
        if request.method=='POST':
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            state = request.POST.get('state')
            city = request.POST.get('city')
            address = request.POST.get('address')
            feedback = request.POST.get('feedback')
        
        data = {'phone': phone,'email' :email, 'state':state,'city':city,'address':address,'feedback':feedback}
      
      
    except:
        pass

    return render(request, "contact.html",data)



def purchase(request):
    return render(request,"purchase.html")