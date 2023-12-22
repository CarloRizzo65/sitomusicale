from django import forms
from .models import Evento, Commenti
from django.contrib import messages
from django.core.exceptions import ValidationError
from datetime import datetime
from captcha.fields import CaptchaField

class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', datetime.today().strftime("%Y-%m-%d"))

class PrenotaEventoForm(forms.ModelForm):

    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome_contatto'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'nome_contatto', 'placeholder':'Nome*'})
        self.fields['cognome_contatto'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'cognome_contatto', 'placeholder':'Cognome*'})
        self.fields['email_contatto'].widget.attrs.update({'class':'form-control input_elem', 'pattern':"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$",'required':False,'autocomplete': 'email', 'placeholder':'Email'})
        self.fields['citta_contatto'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'citta_contatto', 'placeholder':'Città*'})
        self.fields['provincia_contatto'].widget.attrs.update({'class':'form-control input_elem', 'pattern':"^[a-zA-Z]{2}$", 'required':True,'autocomplete': 'provincia_contatto', 'placeholder':'Sigla della provincia*'})
        self.fields['cellulare_contatto'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'cellulare_contatto', 'placeholder':'Cellulare*'})
        self.fields['tipo_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'tipo_evento', 'placeholder':'Tipo di evento (matrimonio, compleanno,...)*'})
        self.fields['luogo_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':False,'autocomplete': 'luogo_evento', 'placeholder':'Nome della sala o del luogo privato'})
        self.fields['citta_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':True,'autocomplete': 'citta_evento', 'placeholder':'Città*'})
        self.fields['provincia_evento'].widget.attrs.update({'class':'form-control input_elem', 'pattern':"^[a-zA-Z]{2}$", 'required':True,'autocomplete': 'provincia_evento', 'placeholder':'Sigla della provincia*'})
        self.fields['indirizzo_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':False,'autocomplete': 'indirizzo_evento', 'placeholder':'Via/Piazza e numero civico'})
        self.fields['data_evento'].widget.attrs.update({'class':'form-control input_elem', 'required':True, 'placeholder':'gg/mm/aaaa*'})
        self.fields['componenti'].widget.attrs.update({'size':3,'class':'form-control input_elem', 'required':True, 'placeholder':'Partecipanti della band all\'evento*'})




    class Meta:
        model = Evento
        fields = ['nome_contatto', 'cognome_contatto','email_contatto', 'citta_contatto', 'provincia_contatto', 'cellulare_contatto',
                  'tipo_evento', 'luogo_evento', 'citta_evento', 'provincia_evento','indirizzo_evento', 'componenti', 'data_evento']
        widgets = {
            'data_evento': DateInput(),
        }


class CommentiForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Commenti
        fields = ['nome','email','commento','captcha']   