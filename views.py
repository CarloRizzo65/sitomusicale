from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FotoCarousel,Evento, Componente, Commenti, FotoPage
from .forms import PrenotaEventoForm, CommentiForm

# Create your views here.
def home(request):
    slides = FotoCarousel.objects.all()
    eventi = Evento.objects.all()
    return render(request, 'home.html',{'slides':slides,'eventi':eventi})

def fotopage(request):
    #foto = FotoPage.objects.all()
    foto = FotoPage.objects.all().order_by('-data_inserimento')[:9]

    form=CommentiForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form=form.save()
            return redirect('gruppo:foto')
    else:
       form =CommentiForm()
    commenti = (Commenti.objects.all().order_by('-data_inserimento')[:3]).values()
    return render (request, 'fotopage.html',{'foto':foto,'form':form,'commenti':commenti})

def videopage(request):
    return render(request, 'videopage.html', {})

def chisiamo(request):
    artisti = Componente.objects.all()
    return render(request, 'chisiamo.html',{'artisti':artisti})

def lavoraconnoi(request):
    if request.method == 'POST':
        form = PrenotaEventoForm(request.POST)
        if form.is_valid():
            artista = form.save()
            messages.success(request,("La tua candidatura è sata inviata con sucesso"))
            return redirect('home')
    else:
        form = PrenotaEventoForm()
    return render(request, 'lavoraconnoi.html', {'form':form})

def prenotaevento(request):
    if request.method == 'POST':
        prenota_form = PrenotaEventoForm(request.POST)
        if prenota_form.is_valid():
            prenota_form.save()
            #messages.success(request, "Prenotazione avvenuta con successo")
            messaggio = "Prenotazione avvenuta con successo"
            return render(request,'prenotaevento.html', {'prenota_form':PrenotaEventoForm(), 'messaggio':messaggio})
    else:
            prenota_form = PrenotaEventoForm()
    return render(request,'prenotaevento.html', {'prenota_form':prenota_form})
