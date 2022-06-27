from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse
from django.contrib import messages
from . models import Note


# Create your views here.
def home(request):
    note = Note.objects.all()
    return render(request, 'home.html',{'note': note})

def update(request, pk):
    if request.method == 'POST':
        data = request.POST.get('updated')
        # print(data)
        instance = Note.objects.get(pk=pk)
        # print(instance.body)
        instance.body = data
        instance.save()
        messages.success(request, 'Successfully updated the Note')
        return redirect('home')

def delete(request, pk):
    instance = Note.objects.get(pk=pk)
    # print(instance.body)
    instance.delete()
    messages.success(request, 'Successfully deleted the Note')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        tit = request.POST.get('tit')
        bod = request.POST.get('bod')
        if (tit == "" or bod == "" ):
            messages.warning(request, 'Ooops ! Unable to submit form due to empty fields.')
            return redirect('create')
        else:
            instance = Note(title = tit, body = bod)
            instance.save()
            messages.success(request,'Your have Successfully created a new Note')
            return redirect('home')

    return render(request, 'create.html')

def show(request, pk):
   note = Note.objects.get(pk=pk)
   return render(request, 'show.html',{'note': note})