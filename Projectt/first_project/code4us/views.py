from django.shortcuts import render
from django.http import HttpResponse

Kategori=['Dünya Klasik','Çocuk','Polisiye','Fantastik','Türk Klasik','Romantik','Korku-Gerilim','Macera']


def home(request):
    data={
        'Kategoriler':Kategori
    }
    return render(request,'index.html',data)

def books(request):
    return render(request,'books.html')
