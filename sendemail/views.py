from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.mail import send_mail
from datetime import datetime


def api(request):
     name = request.GET.get('name')
     receiver=request.GET.get('receiver')
     sat=request.GET.get('sat')
     minut=request.GET.get('minut')
     frizer=request.GET.get('frizer')
     datum=request.GET.get('datum')

     subject=" Informacije o zakazanom terminu | SanjaM Studio "# The theme
     from_email='sanjamuskistudio@gmail.com'# Give a person
     to_email=receiver# The recipient
     print(to_email)
     message="Dobar dan {0}".format(name) + ". \n\n" + "Datum vaseg sisanja je {0}".format(datum) + " u {0}".format(sat) + ":{0}".format(minut) + ". Vas frizer je {0}".format(frizer) + ". \n\n" + "Za otkazivanje termina molimo Vas pozovite  +381691303083."
     print(message)
     try:
          send_mail(subject,message,from_email,[to_email])# call mail Of send_mail Function to send mail
     except Exception as e:
          print(e)
     return HttpResponse(' The mail was sent successfully ')
