from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import DiabetesModel#,Profile

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'autocomplete':'off'}))

    def clean(self):
        cleaned_data = super().clean()


class DiabetesForm(forms.Form):

    Pregnancies = forms.IntegerField(help_text="No. of pregnancies, if Any")
    Glucose = forms.IntegerField(help_text="Blood Glucose level")
    BloodPressure = forms.IntegerField(help_text="In mm Hg")
    SkinThickness = forms.IntegerField(help_text="Skin thickness of armpit, neck or groin")
    Insulin  = forms.IntegerField(help_text="In uIU/mL")
    BMI = forms.FloatField(help_text="Body Mass Index")
    Diabetes_Pedigree_Function = forms.FloatField(help_text="How many family members had diabetes")

    def clean(self):
        cleaned_data = super().clean()


class HeartForm(forms.Form):
    Chest_Pain = forms.IntegerField(help_text="Chest pain type: 1 = typical angina; 2 = atypical angina; 3 = non-angina pain; 4 = asymptomatic")
    Systolic_blood_pressure = forms.IntegerField(help_text="in mm Hg")
    cholesterol  = forms.IntegerField(help_text="Serum cholesterol in mg/dl")
    Fasting_blood_sugar = forms.IntegerField(help_text="fsb > 120 mg/dl (1 = true; 0 = false)")
    Resting_electrocardiographic_results = forms.IntegerField(help_text=" 0 = normal; 1 = having ST-T wave abnormality; 2 = left ventricular hypertrophy")
    Maximum_heart_rate = forms.IntegerField(help_text="Maximum heart rate achieved")
    Exercise_induced_angina = forms.IntegerField(help_text=" (1 = yes; 0 = no)")
    ST_depression = forms.FloatField(help_text="Exercise-induced ST depression relative to rest")
    slope_of_ST_segment = forms.IntegerField(help_text="1 = upsloping; 2 = flat;3 = downsloping")
    major_vessels  = forms.IntegerField(help_text="0-3")
    Exercise_Thallium_heart = forms.IntegerField(help_text="3 = normal; 6 = fixed defect; 7 = reversible defect")


    def clean(self):
        cleaned_data = super().clean()


class BreastForm(forms.Form):
    radius_mean = forms.FloatField()
    texture_mean = forms.FloatField()
    perimeter_mean = forms.FloatField()
    area_mean = forms.FloatField()	
    smoothness_mean = forms.FloatField()
    compactness_mean = forms.FloatField()	
    concavity_mean = forms.FloatField()	
    concave_points_mean  = forms.FloatField()
    symmetry_mean = forms.FloatField()	
    fractal_dimension_mean = forms.FloatField()
    radius_se = forms.FloatField()
    texture_se = forms.FloatField()
    perimeter_se = forms.FloatField()
    area_se = forms.FloatField()
    smoothness_se = forms.FloatField()
    compactness_se = forms.FloatField()
    concavity_se = forms.FloatField()
    concave_points_se = forms.FloatField()
    symmetry_se = forms.FloatField()
    fractal_dimension_se = forms.FloatField()
    radius_worst = forms.FloatField()
    texture_worst = forms.FloatField()
    perimeter_worst = forms.FloatField()
    area_worst = forms.FloatField()
    smoothness_worst = forms.FloatField()
    compactness_worst = forms.FloatField()
    concavity_worst = forms.FloatField()
    concave_points_worst = forms.FloatField()
    symmetry_worst = forms.FloatField()
    fractal_dimension_worst = forms.FloatField()

    def clean(self):
        cleaned_data = super().clean()


class CardioForm(forms.Form):

    height = forms.IntegerField(help_text="In centimeters")
    weight = forms.IntegerField(help_text="In Kilograms")
    arterial_pressure_high = forms.IntegerField(help_text="Systolic Blood Pressure")
    arterial_pressure_low = forms.IntegerField(help_text="Diastolic Blood Pressure")
    cholesterol = forms.IntegerField(help_text="1=normal, 2=high, 3=very high")
    glucose = forms.IntegerField(help_text="1=normal, 2=high, 3=very high")
    smoke = forms.IntegerField(help_text="Enter 0 if you dont smoke, and 1 if you do")
    alcohol = forms.IntegerField(help_text="Enter 0 if dont consume alcohol, and 1 if you do")
    active = forms.IntegerField(help_text="Enter 0 if you do not exercise regularly, and 1 if you do")

    def clean(self):
        clean_data = super().clean()

"""
class DiabetesFormb(forms.ModelForm):

    class Meta:
        model = DiabetesModel
        fields = ('')
"""
