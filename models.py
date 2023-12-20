from django.db import models
from django.utils import timezone
#Per immagine preview in admin
from django.utils.html import mark_safe

from datetime import datetime, date
import locale
locale.setlocale(locale.LC_ALL, 'it')

#Librerie per Resize Img
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

#Per cancellare le immagini
from django_cleanup import cleanup

#Per caricare l'editor di testo avanzato
from ckeditor.fields import RichTextField #Senza la funzione di upload delle immagini
from ckeditor_uploader.fields import RichTextUploadingField #Con la possibilità di fare l'upload delle immagini

#Vado ad importare il validatore tramite regex
from django.core.validators import RegexValidator

# Create your models here.
class Ruolo(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'ruoli'

@cleanup.select
class Componente(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    cognome = models.CharField(max_length=150, null=True, blank=True)
    nickname = models.CharField(max_length=150, null=True, blank=True)
    descrizione = RichTextField(null=True, blank=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='img_componenti/%Y/%m/%d/', default='no-img.png')
    img_resized = ImageSpecField(source='img',
                                      processors=[ResizeToFill(315,315)],
                                      format='PNG',
                                      options={'quality': 60})
    ruolo = models.ForeignKey(Ruolo, related_name='componente', on_delete=models.CASCADE, unique=True)

    def __str__(self):
        nome_completo = f"{self.nome} {self.cognome}"
        return f"{self.nickname if self.nickname is not None else nome_completo}"
    
    class Meta:
        verbose_name_plural = 'componenti'

    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')
    

@cleanup.select
class Evento(models.Model): 
    nome_contatto = models.CharField(max_length=150, null=True, blank=True)
    cognome_contatto = models.CharField(max_length=150, null=True, blank=True)
    email_contatto = models.EmailField(max_length = 254)
    citta_contatto = models.CharField("Città di residenza", max_length=200)
    provincia_contatto = models.CharField("Sigla provincia di residenza", max_length=2, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[A-Za-z]{2}$',
        message='Inserisci la sigla di una provincia (2 lettere)',
    )])
    cellulare_contatto = models.CharField("Cellulare contatto", max_length=15, blank=True, null=True, validators=[RegexValidator(
        regex=r'^\d{,15}$',
        message='Inserisci un numero di cellulare (solo cifre, senza spazi)',
    )])
    tipo_evento = models.CharField("Tipo di evento (matrimonio, compleanno...)",max_length=150, null=True, blank=True)
    luogo_evento = models.CharField("Luogo/nome della sala",max_length=255, null=True, blank=True)
    citta_evento = models.CharField("Città dell'evento", max_length=200)
    provincia_evento = models.CharField("Sigla provincia dell'evento", max_length=2, blank=True, null=True, validators=[RegexValidator(
        regex=r'^[A-Za-z]{2}$',
        message='Inserisci la sigla di una provincia (2 lettere)',
    )])
    indirizzo_evento = models.CharField("Via/Piazza e numero civico",max_length=255, null=True, blank=True)
    dataora_evento = models.DateTimeField(default=timezone.now)
    approvato = models.BooleanField(default=False)
    componenti = models.ManyToManyField(Componente)
    data_inserimento = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    data_modifica = models.DateTimeField(auto_now=True, blank=True,null=True)
    img = models.ImageField(upload_to='img_eventi/%Y/%m/%d/', default='no-image.png', blank=True, null=True)
    descrizione = RichTextField(null=True, blank=True)
    img_resized = ImageSpecField(source='img',
                                      processors=[ResizeToFill(360,360)],
                                      format='PNG',
                                      options={'quality': 60})

    def __str__(self):
        return f"{self.tipo_evento} - {self.dataora_evento.strftime('%A %d %B %Y alle %H:%M')}"
    
    class Meta:
        verbose_name_plural = 'Eventi'

    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')
    
    #Salvo le sigle provincia in Maiuscolo nel DB
    def save(self, *args, **kwargs):
        if self.provincia_contatto:
            self.provincia_contatto = self.provincia_contatto.upper()
        if self.provincia_evento:
            self.provincia_evento = self.provincia_evento.upper()
        if self.dataora_evento:
            self.dataora_evento = None
        # if self.dataora_evento:
        #     arr_data = self.dataora_evento.split("/")
        #     self.dataora_evento = f"{arr_data[2]}/{arr_data[1]}/{arr_data[0]}"
        super(Evento, self).save(*args, **kwargs)
        return None
    
@cleanup.select   
class FotoCarousel(models.Model):
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='img_foto_carousel/%Y/%m/%d/', default='no-image.png')
    img_resized = ImageSpecField(source='img',
                                      processors=[ResizeToFill(360,360)],
                                      format='PNG',
                                      options={'quality': 60})

    def __str__(self):
        return f"{self.img.url}"
    
    class Meta:
        verbose_name_plural = 'Foto del carousel'

    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')

@cleanup.select   
class FotoPage(models.Model):
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='img_foto_page/%Y/%m/%d/', default='no-image.png')
    img_resized = ImageSpecField(source='img',
                                      processors=[ResizeToFill(250,250)],
                                      format='PNG',
                                      options={'quality': 60})

    def __str__(self):
        return f"{self.img.url}"
    
    class Meta:
        verbose_name_plural = 'Foto della foto page'

    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')
    
@cleanup.select   
class Video(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='img_video/%Y/%m/%d/', default='no-image.png')
    img_resized = ImageSpecField(source='img',
                                      processors=[ResizeToFill(250,250)],
                                      format='PNG',
                                      options={'quality': 60})

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = 'Video della video page'

    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="150" />')

@cleanup.select   
class DatiGruppo(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='', default='logo_provvisorio.png')
    descrizione = RichTextField(null=True, blank=True)
    img_resized = ImageSpecField(source='logo',
                                      processors=[ResizeToFill(190,100)],
                                      format='PNG',
                                      options={'quality': 60})

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = 'Dati generali del gruppo'

    def img_preview(self):
        return mark_safe(f'<img src="{self.logo.url}" width="150" />')
    
class Commenti(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)
    evento = models.CharField(max_length=255, null=True, blank=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)
    testo = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.data_inserimento.strftime('%A %d %B %Y alle %H:%M')}"
    
    class Meta:
        verbose_name_plural = 'Commenti'

class LavoraConNoi(models.Model): 
    nome = models.CharField(max_length=150, null=True, blank=True)
    cognome = models.CharField(max_length=150, null=True, blank=True)
    eta = models.PositiveIntegerField("Età",null=True, blank=True)
    email = models.EmailField(max_length = 254)
    esperienza = models.TextField(null=True, blank=True)
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} {self.cognome}"
    
    class Meta:
        verbose_name_plural = 'Lavora con noi'
