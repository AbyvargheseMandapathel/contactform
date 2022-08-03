from django.shortcuts import render,redirect
from .forms import contactform
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.
def home(request):
    form= contactform(request.POST)
    if request.method =='POST':


        if form.is_valid():
            name=(form.cleaned_data['name'])
            email = (form.cleaned_data['email'])
            content = (form.cleaned_data['content'])

            html = render_to_string ('contactform.html',{
                'name':name,
                'email': email,
                'content': content
            })

            print('form valid')
            send_mail('subject','message','abyvarghesemandapathel@gmail.com',['esportsdaily2020@gmail.com'], html_message=html)

            return redirect('home')
        else:
            form=contactform()

    return render (request,'index.html',{'form':form})

