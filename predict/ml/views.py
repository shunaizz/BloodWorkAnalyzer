from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from .models import User,DiabetesModel,Profile,CardioModel,HeartModel,BreastModel
from django.shortcuts import redirect
from .froms import (UserCreateForm,DiabetesForm,
                    ProfileForm,HeartForm,BreastForm,CardioForm)
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core import serializers

from django.urls import reverse_lazy,reverse
from .MlModels.ml import Diabetes,Heart,BreastCancer,Cardio
import numpy as np
import datetime

diabetes_model = Diabetes()
breast_model = BreastCancer()
heart_model = Heart()
cardio_model = Cardio()


class Index(TemplateView):
    template_name = 'index.html'


def profile_view(request,data):

    form = ProfileForm()
    template_name = 'profile.html'

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(pk=data)[0]
            profile = Profile.objects.filter(user=user)[0]
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile.birthdate = form.cleaned_data['birth_date']
            profile.save()
            print('nav ala ka',user.username)
            list = form.cleaned_data
            for i in list:
                print(i,list[i])
            print('first_name',first_name)
            return redirect('login')

    else:
        return render(request,template_name,{'form':form})

    return render(request,template_name,{'form':form})


class SignUp(CreateView):
    template_name = 'ml/signup.html'
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse('ml:profile_create',kwargs={'data':self.object.pk})


def calculateAge(born):
    a = get_user_model()
    today = datetime.date.today()
    try:
        birthday = born.replace(year=today.year)

        # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


@login_required
def Diabetes_view(request): 
    template_name = 'ml/Diabetes.html'

    if request.method == "POST":
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data_list = []
            user = Profile.objects.filter(user=request.user)[0]
            bod = user.birthdate
            age = calculateAge(bod)
            glucose = data['Glucose']
            level = ''  
            if glucose < 110:
                level = 'N'
            else:
                if glucose < 160:
                    level = 'H'
                else:
                    level = 'V'


            for i in data:
                data_list.append(data[i])

            data_list.append(age)

            input_array = np.array([data_list])
            a = diabetes_model.result(input_array)[0]
            data['output'] = a
            DiabetesModel.objects.create(user=request.user, **data)
            # print(a)
            dis = 'Diabetes'

            return redirect(reverse('ml:result',kwargs={'result':a,'model':dis,'level':level}))

    else:
        form = DiabetesForm()
        return render(request,template_name,{'form':form})

    return render(request,template_name,{'form':form})


@login_required
def cardiac_view(request):
    template_name = 'ml/Cardiac.html'

    if request.method == "POST":
        form = HeartForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            input_list = []
            user = Profile.objects.filter(user=request.user)[0]
            bod = user.birthdate
            age = calculateAge(bod)
            print('age',age)
            gender = user.gender
            input_list.append(age)
            if gender == 'male':
                input_list.append(1)
            else:
                input_list.append(0)                
            cholesterol = data['cholesterol']
            level = ''
            if cholesterol < 200:
                level = 'N' 
            else:
                if cholesterol < 300:
                    level = 'H'
                else:
                    level = 'V'

            for i in data:             
                input_list.append(data[i])

            input_array = np.array([input_list])
            input_array = input_array.astype(np.float64)
            print('input array',input_array)

            a = heart_model.result(input_array)[0]
            data['output'] = a
            # print('data',data)
            HeartModel.objects.create(user=request.user, **data)
            dis = 'Cardiac'
            return redirect(reverse('ml:result', kwargs={'result': a, 'model': dis,'level':level}))

    else:
        form = HeartForm()
        return render(request,template_name,{'form':form})
    

@login_required
def breast_view(request):
    template_name = 'ml/bc.html'

    if request.method == "POST":
        form = BreastForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            input_list = []
            for i in data:
                input_list.append(data[i])

            input_array = np.array([input_list])
            input_array = input_array.astype(np.float64)
            a = breast_model.result(input_array)[0]
            data['output'] = a
            BreastModel.objects.create(user=request.user, **data)
            dis = 'Breast' 
            level = 'N'
            return redirect(reverse('ml:result', kwargs={'result': a, 'model': dis, 'level':level}))

    else:
        form = BreastForm()
        # pre_data = Bres
        return render(request, template_name, {'form': form})


@login_required
def cholesterol_view(request): 
    template_name = 'ml/Cardio.html'

    if request.method == "POST":
        form = CardioForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            input_list = []
            user = Profile.objects.filter(user=request.user)[0]
            bod = user.birthdate
            age = calculateAge(bod)
            input_list.append(age)
            gender = user.gender
            # make  a new model entry for cardio
            # new_model = Cardio()
            if gender == 'male':
                input_list.append(1)
            else:
                input_list.append(0)       
            for i in data:
                #print(i)
                j = data[i]
                #print(type(j),j)
                input_list.append(j)
            arterial_pressure_high = data['arterial_pressure_high']
            level = ''
            if arterial_pressure_high < 120:
                level = 'N'
            else:
                if arterial_pressure_high < 140:
                    level = 'H'
                else:
                    level = 'V'

            input_array = np.array([input_list])
            input_array = input_array.astype(np.float64)
            a = cardio_model.result(input_array)[0]
            data['output'] = a
            CardioModel.objects.create(user=request.user, **data)
            dis = 'Obesity' 
            return redirect(reverse('ml:result', kwargs={'result': a, 'model': dis,'level':level}))


    else:
        form = CardioForm()
        pre_data = CardioModel.objects.all().order_by('-created_at')
        return render(request, template_name, {'form': form})


class Result(TemplateView,LoginRequiredMixin):
    template_name = 'ml/result.html'
    links = {
        'Obesity':[['https://www.webmd.com/diet/obesity/default.htm','Understanding Obesity better'],['https://www.healthline.com/nutrition/30-ways-to-lose-weight-naturally','30 Easy Ways to Lose Weight Naturally'],['https://www.structurehouse.com/obesity/','Medical Assistance for Obesity']],
        'Cardiac':[['https://www.webmd.com/heart-disease/default.htm','Understanding Cardiovascular diseases better'],['https://www.healthline.com/health/home-remedies-for-heart-pain#_noHeaderPrefixedContent','Home Remedies for Heart Pain: What Works?'],['https://www.mayoclinic.org/departments-centers/cardiovascular-medicine/sections/overview/ovc-20121933?mc_id=google&campaign=1709906046&geo=1014234&kw=%2Bcardiovascular%20%2Bdisease&ad=440762701598&network=g&sitetarget=&adgroup=101937593906&extension=&target=kwd-297995298665&matchtype=b&device=c&account=1733789621&invsrc=heart&placementsite=enterprise&gclid=CjwKCAiAnvj9BRA4EiwAuUMDf0KZVOPJvm5AIaX5L6DYGB5lQAReWaCciJYFMHjcQs4VFVWnXNlVJxoCDV8QAvD_BwE','Medical Assistance for Cardiovascular Diseases']],
        'Diabetes':[['https://www.webmd.com/diabetes/default.htm','Understanding Diabetes better'],['https://www.healthline.com/nutrition/15-ways-to-lower-blood-sugar','15 Easy Ways to Lower Blood Sugar Levels Naturally'],['https://www.cvs.com/content/health-hub/diabetes?icid=healthhub-resources-diabetes','Medical Assistance for Diabetes']],
        'Breast':[['https://www.webmd.com/breast-cancer/default.htm','Understanding Breast Cancer better'],['https://www.healthline.com/health/breast-cancer/home-remedies-for-breast-cancer#insomnia','Home Remedies for Symptoms of Breast Cancer'],['https://health.ucsd.edu/specialties/cancer/programs/breast/Pages/default.aspx?gclid=Cj0KCQiAwf39BRCCARIsALXWETzSGY0dNZX3ZBnuZbNYlonfV5v4l2oXCx18tMHZMZ8uvRzo71XvzEwaArQ8EALw_wcB','Medical Assistance for Breast Cancer']],
        }
    
    yt_links = {
        'Obesity':[['https://www.youtube.com/watch?v=Aoh7tYBjeGc','Obesity: It’s More Complex than You Think'],['https://www.youtube.com/watch?v=iQUJ1HV0PWc','Obesity, Causes, SIgns and Symptoms, Diagnosis and Treatment.']],
        'Cardiac':[['https://www.youtube.com/watch?v=aXDaBuPSvJs','Heart Disease - Causes, Symptoms and Treatment Options'],['https://www.youtube.com/watch?v=e-Iw_EKz8TI','CHEST PAIN: When to Worry? (Doctors Update) 2020']],
        'Diabetes':[['https://www.youtube.com/watch?v=3GLhwx_G5gE','Five Signs That Could be Symptoms of Diabetes'],['https://www.youtube.com/watch?v=NdsosqVZwcA','Pre-Diabetes: Steps to Gain Control']],
        'Breast':[['https://www.youtube.com/watch?v=jPtCkcILCGU','Breast cancer - causes, symptoms, diagnosis, treatment, pathology'],['https://www.youtube.com/watch?v=ZWqfoBj2bsA','Breast Cancer Type and Stage: What You Need to Know']],
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = context['result']
        b = context['model']
        context['links'] = self.links[b]
        context['yt'] = self.yt_links[b]
        # print('context',context['links'])
        # print('in context',a,b)
        return context


class History(ListView,LoginRequiredMixin):
    template_name = 'ml/history.html'
    context_object_name = 'records'
    
    def get_context_data(self):
        context = super().get_context_data()
        context['model'] = self.model
        context['navModel'] = self.nav_model
        return context

    
    def get_queryset(self):
        self.model = self.kwargs['model']
        user = self.request.user
        self.nav_model = ''
        if self.model == 'Obesity': # Orignal Cardio
            self.nav_model = 'cholesterol'
            return CardioModel.objects.filter(user=user).order_by("-created_at")
        
        elif self.model == 'Cardiac':
            self.nav_model = 'cardiac'
            return HeartModel.objects.filter(user=user).order_by("-created_at")
        
        elif self.model == 'Diabetes':
            self.nav_model = 'diabetes'
            return DiabetesModel.objects.filter(user=user).order_by("-created_at")
        
        elif self.model == 'Breast':
            self.nav_model = 'breast'
            return BreastModel.objects.filter(user=user).order_by("-created_at")


class Record(TemplateView,LoginRequiredMixin):
    template_name = "ml/HistoryPage.html"
    context_object_name = 'query'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        model = context['model']
        pk = context['pk']
        # print('model',model,pk)
        if model == 'Obesity': # Orignal Cardio
            qury = CardioModel.objects.filter(pk=pk)
            obj = serializers.serialize("python",qury)
            op = qury[0].output
            cnt = 1
            data = []
            for object in obj:
                for field_name, field_value in object['fields'].items():
                    # print (field_name,'->', field_value)
                    if cnt > 1 and cnt < 11:
                        data.append([field_name,field_value])
                    cnt+=1
            context['data'] = data
            context['output'] = op


        elif model == 'Cardiac':
            qury = HeartModel.objects.filter(pk=pk)
            obj = serializers.serialize("python",qury)
            op = qury[0].output
            cnt = 1
            data = []
            for object in obj:
                for field_name, field_value in object['fields'].items():
                    # print (field_name,'->', field_value)
                    if cnt > 1 and cnt < 14:
                        data.append([field_name,field_value])
                    cnt+=1
            context['data'] = data
            context['output'] = op


        elif model == 'Diabetes':
            qury = DiabetesModel.objects.filter(pk=pk)
            obj = serializers.serialize("python",qury)
            op = qury[0].output
            cnt = 1
            data = []
            for object in obj:
                for field_name, field_value in object['fields'].items():
                    # print (field_name,'->', field_value)
                    if cnt > 1 and cnt < 10:
                        data.append([field_name,field_value])
                    cnt+=1
            context['data'] = data
            context['output'] = op


        elif model == 'Breast':
            qury = BreastModel.objects.filter(pk=pk)
            obj = serializers.serialize("python",qury)
            op = qury[0].output
            cnt = 1
            data = []
            for object in obj:
                for field_name, field_value in object['fields'].items():
                    # print (field_name,'->', field_value)
                    if cnt > 1 and cnt < 30:
                        data.append([field_name,field_value])
                    cnt+=1
            context['data'] = data
            context['output'] = op
        # context['query'] = qury
        return context


