from django.db import models
from django import forms

# Create your models here.
class adminregister(models. Model):
    email = models.CharField(max_length= 200)
    password = models.CharField(max_length= 200)



class sliderdata(models. Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    background_img = models.ImageField(upload_to='slider-media/')


class SliderDataForm(forms.ModelForm):
    class Meta:
        model = sliderdata
        fields = ['title', 'description', 'background_img']


class offerdata(models. Model):
    offer_icon = models.ImageField(upload_to='slider-media/' , blank=True, null=True)
    offer_heading = models.CharField(max_length = 200)
    offer_des = models.CharField(max_length = 1000)


class OfferDataForm(forms.ModelForm):
    class Meta:
        model = offerdata
        fields = ['offer_icon', 'offer_heading', 'offer_des']



class categorydata(models. Model):
    ourcat = models.CharField(max_length = 200)


class catformdata(forms.ModelForm):
    class Meta:
        model = categorydata
        fields = ['ourcat']



class blogdata(models. Model):
    feature_img = models.ImageField(upload_to='slider-media/' , blank=True, null=True)
    post_title = models.CharField(max_length = 200)
    post_date = models.DateField()
    post_description = models.CharField(max_length = 10000)
    categories = models.ManyToManyField(categorydata)
    auth_name = models.CharField(max_length= 200 , default=" ")
    about_des = models.CharField(max_length = 200, default=" ")


class BlogFormData(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=categorydata.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = blogdata
        fields = ['feature_img', 'post_title', 'post_date' , 'post_description' , 'categories' , 'auth_name', 'about_des']