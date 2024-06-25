from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import tensorflow.keras as k
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
from django.conf import settings
from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
global scaler
from PIL import Image
import torchvision.transforms as transforms
import torch
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
import os
import numpy as np




def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index1')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def index1(request):
    return render(request, 'index1.html')
def predictImage(request):
    if request.method == 'POST' and request.FILES.get('filePath'):
        # Handle file upload
        fileObj = request.FILES['filePath']
        fs = FileSystemStorage()
        filePathName = fs.save(fileObj.name, fileObj)
        filePath = os.path.join(settings.MEDIA_ROOT, filePathName)
        image = load_img(filePath, target_size=(224, 224))
        image = np.expand_dims(image, axis=0)
        model = load_model('vgg_mod.h5')
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)

        classname=['Corn_leaf_spot','Grape_Black_rot','Healthy','Potato_Early_blight','Strawberry_Leaf_scorch']
        context = {'filePathName': fs.url(filePathName), 'predictedLabel':classname[predicted_class] }
        return render(request, 'index1.html', context)

    return HttpResponse("Invalid request")