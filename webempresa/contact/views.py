from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms

# Create your views here.
def Contact(request):
    contact_form=ContactForms()

    if request.method=="POST":
        contact_form=ContactForms(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')
        #Enviamos correo y redireccionamos
        email = EmailMessage(
            "Asunto: la cafeteira te saluda",
            "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
            "no-contestar@inbox.mailtrap.io",
            ["pechenestiven@gmail.com"],
            reply_to=[email]
        )
        try:
        #Todo ok

            email.send()
            return redirect(reverse('contact')+'?ok')

        except:
        #Algo no ha ido bien
            return redirect(reverse('contact')+'?fail')


    



    return render(request,'contact/contact.html',{'form':contact_form}) 