from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    choices = [('male','male'),('female','female')]
    gender = models.CharField(max_length=10,null=True,blank=True,choices=choices)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class DiabetesModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.FloatField()
    Diabetes_Pedigree_Function = models.FloatField()
    output = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.created_at) + ' ' + str(self.output)


class HeartModel(models.Model): #Cardiac
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Chest_Pain = models.IntegerField()
    Systolic_blood_pressure = models.IntegerField()
    cholesterol  = models.IntegerField()
    Fasting_blood_sugar = models.IntegerField()
    Resting_electrocardiographic_results = models.IntegerField()
    Maximum_heart_rate = models.IntegerField()
    Exercise_induced_angina  = models.IntegerField()
    ST_depression = models.FloatField()
    slope_of_ST_segment = models.IntegerField()
    major_vessels = models.IntegerField()
    Exercise_Thallium_heart = models.IntegerField()
    output = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.created_at) + ' ' + str(self.output)



class BreastModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    radius_mean = models.FloatField()
    texture_mean = models.FloatField()
    perimeter_mean = models.FloatField()
    area_mean = models.FloatField(default=0.0)	
    smoothness_mean = models.FloatField()
    compactness_mean = models.FloatField()	
    concavity_mean = models.FloatField()	
    concave_points_mean	 = models.FloatField()
    symmetry_mean = models.FloatField()	
    fractal_dimension_mean = models.FloatField()
    radius_se = models.FloatField()
    texture_se = models.FloatField()
    perimeter_se = models.FloatField()
    area_se = models.FloatField()
    smoothness_se = models.FloatField()
    compactness_se = models.FloatField()
    concavity_se = models.FloatField()
    concave_points_se = models.FloatField()
    symmetry_se = models.FloatField()
    fractal_dimension_se = models.FloatField()
    radius_worst = models.FloatField()
    texture_worst = models.FloatField()
    perimeter_worst = models.FloatField()
    area_worst = models.FloatField()
    smoothness_worst = models.FloatField()
    compactness_worst = models.FloatField()
    concavity_worst = models.FloatField()
    concave_points_worst = models.FloatField()
    symmetry_worst = models.FloatField()
    fractal_dimension_worst = models.FloatField()

    created_at = models.DateTimeField(default=datetime.datetime.now())
    output = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return str(self.created_at) + ' ' + str(self.output)


class CardioModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    height = models.IntegerField()
    weight = models.IntegerField()
    arterial_pressure_high = models.IntegerField()
    arterial_pressure_low = models.IntegerField()
    cholesterol = models.IntegerField()
    glucose = models.IntegerField()
    smoke = models.IntegerField()
    alcohol = models.IntegerField()
    active = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.datetime.now())
    output = models.IntegerField(null=True,blank=True)

    def __str__(self):
       return str(self.created_at) + ' ' + str(self.output)



