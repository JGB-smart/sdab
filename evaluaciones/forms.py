from django import forms
from evaluaciones.models import Entregas,Evaluaciones
from django.contrib.auth.models import User

class EntregaTestForm(forms.ModelForm):
    
    class Meta:
        model = Entregas
        fields = '__all__'

    mensaje = forms.CharField(label="Comentar",widget=forms.Textarea(attrs={'class': 'form-control','id': 'textAreaExample','rows': '4'}))
    test = forms.ModelChoiceField(label=False,queryset=Evaluaciones.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))
    user = forms.ModelChoiceField(label=False,queryset=User.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))
    calificacion = forms.ModelChoiceField(label=False,queryset=Entregas.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))