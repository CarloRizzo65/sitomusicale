from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FotoCarousel,Evento, Componente
from .forms import PrenotaEventoForm

# Create your views here.
def home(request):
    slides = FotoCarousel.objects.all()
    eventi = Evento.objects.all()
    return render(request, 'home.html',{'slides':slides,'eventi':eventi})

def fotopage(request):
    eventi = Evento.objects.all()
    return render(request, 'fotopage.html', {'eventi':eventi})

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
            #Creo un nuovo oggetto utente ma non lo salvo
            #new_user = user_form.save(commit=False)
            #Setto la password
            #new_user.set_password(user_form.cleaned_data['password']) #Django codifica la password in SHA256
            #Ora posso salvare in nuovo utente
            prenota_form.save()
            #messages.success(request, "Prenotazione avvenuta con successo")
            messaggio = "Prenotazione avvenuta con successo"
            #Dopo aver salvato il nuvo utente posso prendere l'id a creare una nuova riga nella tabella profilo con l'id utente appena creato
            #Profilo.objects.create(user=new_user)
            #return redirect('prenotaevento', blog.id)
            #return render(request, 'prenotaevento.html')
            return render(request,'prenotaevento.html', {'prenota_form':PrenotaEventoForm(), 'messaggio':messaggio})
    else:
            prenota_form = PrenotaEventoForm()
    return render(request,'prenotaevento.html', {'prenota_form':prenota_form})
