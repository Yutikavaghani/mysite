from django.shortcuts import render, redirect
from myadminapp.models import adminregister
from myadminapp.models import sliderdata , offerdata , categorydata , blogdata
from myadminapp.models import SliderDataForm , OfferDataForm , catformdata , BlogFormData
import base64

# Create your views here.

def registerdata(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        if adminregister.objects.filter(email=email).exists():
            return render(request, 'admin-registerdata.html', {'error_message': 'Email already registered'})


        mydata = adminregister.objects.filter(email=email, password=password)

        if mydata.count() > 0:
            return redirect('/adminindex')
        
        else:
            encode_text = base64.b64encode(password.encode()).decode()

            obj = adminregister(
                email=email, 
                password=encode_text
            )

            obj.save()
            return redirect('/adminindex')

    return render(request, 'admin-registerdata.html')


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        encode_text = base64.b64encode(password.encode()).decode()
        print(encode_text)

        rgsdata = adminregister.objects.filter(email=username, password=password)
        
        if(rgsdata.count() == 1):

            admin = rgsdata.get()
            request.session['username'] = admin.email
            print(admin.email)
            return redirect('/adminindex')
        else:
            err_msg = 'Invalid Username or Password'
            return render(request, 'admin-login.html', {'err_msg': err_msg})
        
    return render(request, 'admin-login.html')


def adminindex(request):
    if 'username' not in request.session:
        return redirect('/admin-login')
    
    username = request.session['username']  

    return render(request, 'adminindex.html' , {'data': username})


def viewdata(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    allcontactdata = adminregister.objects.all().values()
    print(allcontactdata)

    username = request.session['username']  

    return render(request, 'admin-viewdata.html', {'mydata': allcontactdata , 'data': username})


def deletedata(request, pk):
    user_data = adminregister.objects.get(id=pk)
    user_data.delete()
    return redirect('/admin-viewdata')


def edit_data(request, pk):
    obj = adminregister.objects.filter(id=pk).get()
    
    if request.method == "POST":
        obj.email = request.POST["email"]
        obj.password = request.POST["password"]
        
        obj.save()
        return redirect('/admin-viewdata')

    return render(request, "admin-registerdata.html", {'mydata': obj})


def slideradddata(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 

    form = SliderDataForm()

    if request.method == "POST":

        form = SliderDataForm(request.POST, request.FILES)
        form.save()

        # title = request.POST.get('title')
        # description = request.POST.get('description')
        # background_img = request.FILES.get('background_img') 

        # Save the data into the database
        # obj = sliderdata (
        #     title = title,
        #     description = description,
        #     background_img = background_img
        # )

        # obj.save()

    return render(request, 'slider-add-data.html', {'data': username})



def slider(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 

    data = sliderdata.objects.all()

    return render(request, 'slider-dataview.html', {'slidedata': data , 'data': username})

def slider_delete(request, pk):
    user_data = sliderdata.objects.get(id=pk)
    user_data.delete()

    return redirect('/slider-viewdata/')

def slider_edit(request, pk):
    obj = sliderdata.objects.filter(id=pk).get()
    
    if request.method == "POST":
        obj.title = request.POST["title"]
        obj.description = request.POST["description"]
        
        # Check if a file is uploaded
        if 'background_img' in request.FILES:
            obj.background_img = request.FILES['background_img']
        
        obj.save()
        return redirect('/slider-viewdata/')

    return render(request, "slider-add-data.html", {'mydata': obj})


# ......We Offer.........

def offer_add(request):

    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 

    form = OfferDataForm()

    if request.method == "POST":

        form = OfferDataForm(request.POST, request.FILES)
        form.save()

    return render(request, 'offer-add-data.html', {'data': username})


def offer_view(request):

    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 

    data = offerdata.objects.all()

    return render(request, 'offer-view-data.html', {'offerdata': data , 'data': username})

def offer_delete(request, pk):
    user_data = offerdata.objects.get(id=pk)
    user_data.delete()

    return redirect('/offer-view/')

def offer_edit(request, pk):
    obj = offerdata.objects.filter(id=pk).get()
    
    if request.method == "POST":
        obj.offer_heading = request.POST["offer_heading"]
        obj.offer_des = request.POST["offer_des"]
        
        # Check if a file is uploaded
        if 'offer_icon' in request.FILES:
            obj.offer_icon = request.FILES['offer_icon']
        
        obj.save()
        return redirect('/offer-view/')

    return render(request, "offer-add-data.html", {'mydata': obj})


# .......Category.......

def category_add(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 
    form = catformdata()

    if request.method == "POST":
        form = catformdata(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category-view/')


    return render(request, 'category-add.html', {'data': username, 'form': form})


def category_view(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 

    data = categorydata.objects.all()

    return render(request, "category-view.html" , {'ourcategorydata': data , 'data': username})

def cat_delete(request, pk):
    user_data = categorydata.objects.get(id=pk)
    user_data.delete()

    return redirect('/category-view/')

def cat_edit(request, pk):
    obj = categorydata.objects.filter(id=pk).get()
    
    if request.method == "POST":
        obj.ourcat = request.POST["ourcat"]
        
        obj.save()
        return redirect('/category-view/')

    return render(request, "category-add.html", {'mydata': obj})


# ..........Blog Post...........

def blog_add(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username'] 
    categories = categorydata.objects.all()

    form = BlogFormData()

    if request.method == "POST":
        form = BlogFormData (request.POST, request.FILES)
        if form.is_valid():
            blog_instance = form.save(commit=False)
            blog_instance.save()
            form.save_m2m()  # Save many-to-many relationships (categories)
            return redirect('/blog-view/')

        # form.save()

    return render(request, 'blog-add.html' , {'data': username , 'form': form, 'categories': categories})
 

def blog_view(request):
    if 'username' not in request.session:
        return redirect('/admin-login')

    username = request.session['username']

    email = request.session['username'] 
    author_name = email.split('@')[0]

    data = blogdata.objects.all()

    return render(request, 'blog-view.html' , {'blogdata': data , 'data': username, 'authpr_name': author_name})

def blog_delete(request, pk):
    user_data = blogdata.objects.get(id=pk)
    user_data.delete()

    return redirect('/blog-view/')

def blog_edit(request, pk):
    obj = blogdata.objects.get(id=pk)
    categories = categorydata.objects.all()

    if request.method == "POST":
        form = BlogFormData(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            blog_instance = form.save(commit=False)
            blog_instance.save()
            form.save_m2m()  # Save many-to-many relationships (categories)
            return redirect('/blog-view/')
    else:
        form = BlogFormData(instance=obj)

    return render(request, "blog-add.html", {'mydata': obj, 'form': form , 'categories': categories})


def contact_detail(request):
    return render(request, 'contact-detail.html')

