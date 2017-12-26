# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime



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
                msg={'ta':'try agin'}
            return render(request,'passwordNotTrue.html')


    else:
        form = PersonLoginForm()
        arg = {'form': form}
        return render(request, 'login.html', arg)


def logoutses(request):
    logout(request)
    return redirect('/')

#

def showDrugInformation(request):

        if request.method == 'POST':
            form = DrugNameForm(request.POST)
            if form.is_valid():
                Name = form.cleaned_data['Name']
                if Drug.objects.filter(Commercial_name=Name).exists():
                    cn = Drug.objects.filter(Commercial_name=Name).values('Commercial_name').first()
                    gn = Drug.objects.filter(Commercial_name=Name).values('Generic_name').first()
                    dose = Drug.objects.filter(Commercial_name=Name).values('Dose').first()
                    se = Drug.objects.filter(Commercial_name=Name).values('Side_effects').first()
                    htu = Drug.objects.filter(Commercial_name=Name).values('How_to_use').first()
                    di = Drug.objects.filter(Commercial_name=Name).values('Drug_interactions').first()
                    c = Drug.objects.filter(Commercial_name=Name).values('Compositions').first()
                    p = Drug.objects.filter(Commercial_name=Name).values('Price').first()
                    nop = Drug.objects.filter(Commercial_name=Name).values('Necessity_of_prescription').first()
                    arg = {'cn': cn.get('Commercial_name'), 'gn':gn.get('Generic_name'),'dose': dose.get('Dose'), 'se': se.get('Side_effect'), 'htu': htu.get('How_to_use'), 'di': di.get('Drug_interactions'), 'c': c.get('Compositions'), 'p': p.get('Price'), 'nop': nop.get('Necessity_of_prescription')}
                    return render(request, 'drug_info.html', arg)
                else:
                    return render(request,'DrugNotExist.html')

        else:
                form = DrugNameForm()
                arg = {'form': form}
                print(request.user)
                return render(request, 'drug_info.html', arg)

#
def showDrugstoreInformation(request):
    if request.method == 'POST':
        form = DrugstoreNameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            if DrugStore.objects.filter(name=name).exists():
                ad=DrugStore.objects.filter(name=name).values('address_list').first().get('address_list')
                if AddressOfDrugstore.objects.filter(postal_code=ad).exists():
                    bn=AddressOfDrugstore.objects.filter(postal_code=ad).values('block_number').first()
                    a = AddressOfDrugstore.objects.filter(postal_code=ad).values('alley').first()
                    s = AddressOfDrugstore.objects.filter(postal_code=ad).values('street').first()
                    c=AddressOfDrugstore.objects.filter(postal_code=ad).values('city').first()
                    t = AddressOfDrugstore.objects.filter(postal_code=ad).values('tel').first()
                    arg={'bn':bn.get('block_number'),'a':a.get('alley'),'s':s.get('street'),'c':c.get('city'),'t':t.get('tel'),}
            return render(request, 'drugstore_info.html', arg)
    else:
        form = DrugstoreNameForm()
        arg = {'form': form}
        return render(request, 'drugstore_info.html', arg)

@login_required(login_url='/loginses')
def makeOrder(request):
    if request.method == 'POST':
        form = ordersForm(request.POST)
        if form.is_valid():
            drug_name = form.cleaned_data['Drug_name']
            drugstore_name = form.cleaned_data['Drugstore_name']
            no=form.cleaned_data['Number']
            if Drug.objects.filter(Commercial_name=drug_name).exists() or Drug.objects.filter(Generic_name=drug_name).exists():
                c = Drug.objects.values('Commercial_name')
                if DrugStore.objects.filter(drug_code=c).exists()and DrugStore.objects.filter(name=drugstore_name).exists():
                    d=Drug.objects.get(Commercial_name=drug_name)
                    om=OrderModel(drug=d,quantity=no)
                    om.save()
                    a=getattr(om,'id')
                    w=OrderModel.objects.filter(id=a).values('drug').first()
                    q=OrderModel.objects.filter(id=a).values('quantity').first().get('quantity')
                    q=OrderModel.objects.filter(id=a).values('drug').first().get('drug')

                    d=Drug.objects.filter(Commercial_name=q).first()
                    order = Order(date=datetime.now(),
                                  drug_store=form.cleaned_data['Drugstore_name'].first(),
                                  )
                    order.save()
                    return render(request, 'orderAdded.html')
                #else:
                return render(request, 'orderNotExist.html')
    else:
        form = ordersForm()
        arg = {'form': form}
        return render(request, 'orders.html', arg)
def showDrugsInDrugstore(request):
    arg={}
    global j
    if request.method == 'POST':
        form = whereISDrugForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['Drug_name']
            d=Drug.objects.filter(Commercial_name=name).values('Commercial_name')
            latest_question_list = DrugStore.objects.order_by('-drug_code')
            if Drug.objects.filter(drug_code=d).exists():
                output = ', '.join([q.drug_code for q in latest_question_list].first())
            return HttpResponse(output)
            # for i in DrugStore.objects.all():
            #     if Drug.objects.filter(drug_code=d).exists():
            #         j=j+1
            #         arg['j']=i.filter(drug_code=d).values('name').first().get('name')
            # return render(request,'whereIsDrud.html',arg)
        else:
            return HttpResponse('no')
    else:
        form = whereISDrugForm()
        arg = {'form': form}
        return render(request, 'whereIsDrug.html', arg)

