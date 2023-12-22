from django.contrib import admin
from .models import Ruolo, Componente, Evento, FotoCarousel, FotoPage, Video, DatiGruppo, Commenti, LavoraConNoi
from django.db import models
import locale
locale.setlocale(locale.LC_ALL, 'it')
# from django import forms
# from sitomusicale.widgets import PastCustomDatePickerWidget
# Register your models here.

@admin.register(Ruolo)
class RuoloAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']
    list_display_links = ['__str__']
    list_editable = ['nome']

@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ['__str__','nome','cognome', 'nickname', 'img_preview','ruolo','data_modifica']
    search_fields = ['nome', 'cognome', 'nickname','data_modifica']
    list_filter = ['nome', 'cognome', 'nickname','data_modifica']
    readonly_fields = ['img_preview']
    list_display_links = ['__str__']
    list_editable = ['nome','cognome', 'nickname','ruolo']

@admin.register(FotoCarousel)
class FotoCarouselAdmin(admin.ModelAdmin):
    list_display = ['img_preview','data_modifica']
    search_fields = ['data_modifica']
    list_filter = ['data_modifica']
    readonly_fields = ['img_preview']

@admin.register(FotoPage)
class FotoPageAdmin(admin.ModelAdmin):
    list_display = ['img_preview','data_modifica']
    search_fields = ['data_modifica']
    list_filter = ['data_modifica']
    readonly_fields = ['img_preview']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['img_preview','nome','link','img_preview','data_modifica']
    search_fields = ['nome', 'link', 'data_modifica']
    list_filter = ['nome', 'link', 'data_modifica']
    readonly_fields = ['img_preview']
    list_editable = ['nome','link']

@admin.register(DatiGruppo)
class DatiGruppoAdmin(admin.ModelAdmin):
    list_display = ['__str__','nome','img_preview','descrizione','data_modifica']
    search_fields = ['nome','data_modifica']
    list_filter = ['nome','data_modifica']
    readonly_fields = ['img_preview']
    list_display_links = ['__str__']
    list_editable = ['nome']

@admin.register(Commenti)
class CommentiAdmin(admin.ModelAdmin):
    list_display = ['__str__','nome','commento','email','data_modifica']
    search_fields = ['nome','commento','data_modifica']
    list_filter = ['nome','commento','data_modifica']
    list_display_links = ['__str__']
    list_editable = ['nome','commento','email']

@admin.register(LavoraConNoi)
class LavoraConNoiAdmin(admin.ModelAdmin):
    list_display = ['__str__','nome','cognome', 'email', 'eta','data_modifica']
    search_fields = ['nome', 'cognome', 'email','eta','data_modifica']
    list_filter = ['nome', 'cognome', 'email','eta','data_modifica']
    list_display_links = ['__str__']
    list_editable = ['nome','cognome', 'email','eta']

@admin.register(Evento)
class EventiAdmin(admin.ModelAdmin):

    list_display = ['__str__','nome_contatto','cognome_contatto', 'email_contatto', 'citta_contatto','provincia_contatto','cellulare_contatto','tipo_evento', 'luogo_evento','citta_evento',
                    'provincia_evento','indirizzo_evento','data_evento', 'approvato','img_preview','data_inserimento','data_modifica']
    search_fields = ['nome_contatto', 'cognome_contatto', 'email_contatto','citta_contatto','provincia_contatto',
                     'cellulare_contatto','tipo_evento', 'luogo_evento','citta_evento','provincia_evento','indirizzo_evento','data_evento','data_modifica']
    list_filter = ['nome_contatto', 'cognome_contatto', 'email_contatto','citta_contatto','provincia_contatto','cellulare_contatto','tipo_evento', 'luogo_evento','citta_evento','provincia_evento','indirizzo_evento','data_evento','approvato','data_modifica']
    list_display_links = ['__str__']
    readonly_fields = ['img_preview','data_evento']
    list_editable = ['nome_contatto','cognome_contatto', 'email_contatto','citta_contatto','provincia_contatto','cellulare_contatto','tipo_evento', 'luogo_evento','citta_evento','provincia_evento','indirizzo_evento','approvato']
    