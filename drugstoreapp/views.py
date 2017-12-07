# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

    # if requests.method=='POST':
    #         user=authenticate(email=requests.POST['email'],password=requests.POSt['password'])
    #         login(requests,user)
    #         render(requests,'home.html')


def signup(request):
    if request.method == 'POST':
        form = PersonSignUpForm(request.POST)
        if form.is_valid():
            if Person.objects.filter(email=form.cleaned_data['email']).exists() or Person.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request,'userExist.html')
            person = Person(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            email=form.cleaned_data['email'],
                            username=form.cleaned_data['username'])
            person.set_password(form.cleaned_data['password'])
            person.save()
            arg={'username':form.cleaned_data['username']}

            if form.cleaned_data['are_you_mariz']:
                g = Group.objects.get(name='patiant')
                person.groups.add(g)

        return render(request, 'userPage.html',arg)
    else:
        form = PersonSignUpForm()
        arg = {'form': form}
        return render(request, 'signup.html', arg)


# # def login(request):
# #     return render(request,'login.html')
# def success(request):
#     return render(request, 'success.html')
#
#
def loginses(request):
    if request.method == 'POST':
        form = PersonLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if Person.objects.filter(username=username).exists():
                user = Person.objects.get(username=username)

                if user.check_password(password):
                    login(request, user)
                    arg={'username':username}
                    return render(request,'userPage.html',arg)
            return HttpResponse('eee')


    else:
        form = PersonLoginForm()
        arg = {'form': form}
        return render(request, 'login.html', arg)


def logoutses(request):
    logout(request)
    return redirect('/')

#
# @login_required(login_url='/loginses')
def showDrugInformation(request):
    if request.method == 'POST':
        form = DrugNameForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            if Drug.objects.filter(Commercial_name=Name).exists() or Drug.objects.filter(Generic_name=Name).exists():
                cn = Drug.objects.filter(Commercial_name=Name).values('Commercial_name')
                gn = Drug.objects.filter(Commercial_name=Name).values('Generic_name')
                dose = Drug.objects.filter(Commercial_name=Name).values('Dose')
                se = Drug.objects.filter(Commercial_name=Name).values('Side_effects')
                htu = Drug.objects.filter(Commercial_name=Name).values('How_to_use')
                di = Drug.objects.filter(Commercial_name=Name).values('Drug_interactions')
                c = Drug.objects.filter(Commercial_name=Name).values('Compositions')
                p = Drug.objects.filter(Commercial_name=Name).values('Price')
                nop = Drug.objects.filter(Commercial_name=Name).values('Necessity_of_prescription')
                arg = {'cn': Name, 'gn': gn, 'dose': dose, 'se': se, 'htu': htu, 'di': di, 'c': c, 'p': p, 'nop': nop}

                return render(request, 'drug_info.html', arg)
            else:
                return render(request,'DrugNotExist.html')

    else:
            form = DrugNameForm()
            arg = {'form': form}
            print(request.user)
            return render(request, 'drug_info.html', arg)

#
# def showDrugstoreInformation(request):
#     if request.method == 'POST':
#         form = DrugstoreNameForm(request.POST)
#         if form.is_valid():
#             Name = form.cleaned_dagstore.objects.values_list('Alley')
#             B=AddressOfDrugstore.objects.values_list('Block_number')
#             arg={'N':N,'T':T,'C':C,'S':S,'A':A,'B':B}
#             return render(request, 'drugstore_info.html', arg)
#     else:
#         form = DrugstoreNameForm()
#         arg = {'form': form}
#         return render(request, 'drugstore_info.html', arg)

#
def makeOrder(request):
    if request.method == 'POST':
        form = ordersForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Drug_name']
            drugstore_Name = form.cleaned_data['Name']
            if DrugStore.objects.filter(Name=name).exists():
                Code_flag = DrugStore.objects.values_list('Code')
                # if AddressOfDrugstore.objects.filter(Drugstore_Code=Code_flag):
                #     N = DrugStore.objects.values_list('Name')
                #     T = DrugStore.objects.values_list('Telephone')
                #     C = AddressOfDrugstore.objects.values_list('City')
                #     S = AddressOfDrugstore.objects.values_list('Street')
                #     A = AddressOfDrugstore.cleaned_data['Drugstore_name']
            if Drug.objects.filter(Commercial_name=name).exists() or Drug.objects.filter(Generic_name=name).exists():
                c = Drug.objects.values_list('Drug_code')
                if DrugStore.objects.filter(Drug_Code=c).exists() and DrugStore.objects.filter(
                        Name=drugstore_Name).exists():
                    order = Order(patient_email=form.cleaned_data['Email'],
                                  number_of_drug=form.cleaned_data['Number'],
                                  )
                    order.save()
                    return render(request, 'success.html')
    else:
        form = ordersForm()
        arg = {'form': form}
        return render(request, 'orders.html', arg)