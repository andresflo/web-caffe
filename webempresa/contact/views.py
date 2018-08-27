from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form=ContactForm()

    if request.method  == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Todo esta bien enviamos el correo y redireccionamos
            email = EmailMessage(
                "La caffetiera: nuevo mensaje de contacto", #Asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),#Contenido
                "no-contestar-ecc7ae@inbox.mailtrap.io",#Email de origen
                ["lopez.andres@eia.edu.co"],#email de destino
                reply_to=[email]
            )

            try:
                email.send()
                #todo esta bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien rediccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    return render(request,"contact/contact.html", {'form': contact_form})