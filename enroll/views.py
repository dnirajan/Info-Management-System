from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User


# Create your views here.
def addnshow(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            mail = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=mail, password=pw)
            reg.save()
            fm = UserForm()
    else:
        fm = UserForm()
    stud = User.objects.all()
    return render(request, 'addandshow.html', {'form': fm, 'stu': stud})


def delete(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserForm(instance=pi)
    return render(request, 'update.html', {'form': fm})
