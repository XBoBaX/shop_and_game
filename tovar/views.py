from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from games.models import games
import urllib.request, json, urllib.parse
from OP.models import Operative, Price as o_price
from videokarta.models import Videocard, Price as v_price
from proccesor.models import Proc, Price as p_price
from motherboard.models import Motherboard, Price as m_price
from profiles.models import Profile
from buyer.models import buyed

def more(request1):
    print("more")
    id = request1.GET.get('id', '0')
    obj = request1.GET.get('obj', '0')
    if obj == "Motherboard":
        m = Motherboard.objects.get(id=id)
        pr = m_price.objects.get(tovar=m)
    elif obj == "Proc":
        m = Proc.objects.get(id=id)
        pr = p_price.objects.get(tovar=m)
    elif obj == "Videocard":
        m = Videocard.objects.get(id=id)
        pr = v_price.objects.get(tovar=m)
    elif obj == "Operative":
        m = Operative.objects.get(id=id)
        pr = o_price.objects.get(tovar=m)

    return render(request1, 'tovar/index.html', {'gl': 13, 'obj': m, 'pr': pr})


def compex(request1):
    print("hahaha")
    select = request1.POST.get('sel1', 'Выбрать..')
    select2 = request1.POST.get('sel2', 'Выбрать..')
    select3 = request1.POST.get('sel3', 'Выбрать..')
    select4 = request1.POST.get('sel4', 'Выбрать..')
    select5 = request1.POST.get('sel5', 'Выбрать..')
    select6 = request1.POST.get('sel6', 'Выбрать..')
    select7 = request1.POST.get('sel7', 'Выбрать..')
    select8 = request1.POST.get('sel8', 'Выбрать..')
    if select == "":
        select = 'Выбрать..'
    if select2 == "":
        select2 = 'Выбрать..'
    if select3 == "":
        select3 = 'Выбрать..'
    if select4 == "":
        select4 = 'Выбрать..'
    if select5 == "":
        select5 = 'Выбрать..'
    if select6 == "":
        select6 = 'Выбрать..'
    if select7 == "":
        select7 = 'Выбрать..'
    if select8 == "":
        select8 = 'Выбрать..'
    list1 = request1.POST.get('list1', '0')
    list2 = request1.POST.get('list2', '0')
    list3 = request1.POST.get('list3', '0')
    list4 = request1.POST.get('list4', '0')
    ser = request1.POST.get('search', '1')
    ttt = 0
    i = 0
    if list1 == list2 == list3 == list4:
        ttt = 1
    list = []
    if ttt == 1:
        print("all")

        urlA = "https://checklistday.000webhostapp.com/api/processor?name="
        urlA += urllib.parse.quote(ser)
        if select7 != "Выбрать..":
            urlA += "&socket={0}".format(select7)
        if select8 != "Выбрать..":
            urlA += "&cores_from={0}&cores_to={0}".format(select8)
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        print(temp)
        for ch in temp:
            if i >= 30:
                break
            try:
                proc = Proc.objects.get(id=int(ch))
                list.append(proc)
                i += 1
            except Exception:
                t = 1
        urlA = "https://checklistday.000webhostapp.com/api/mother?name="
        urlA += urllib.parse.quote(ser)
        if select3 != "Выбрать..":
            urlA += "&form_factor={0}".format(select3)
        if select4 != "Выбрать..":
            urlA += "&proc_socket={0}".format(select4)
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        print(temp)
        for ch in temp:
            if i >= 30:
                break
            try:
                proc = Motherboard.objects.get(id=int(ch))
                list.append(proc)
                i += 1
            except Exception:
                t = ""
            i+=1
        urlA = "https://checklistday.000webhostapp.com/api/operative?name="
        urlA += urllib.parse.quote(ser)
        if select5 != "Выбрать..":
            urlA += "&v_to={0}&v_from={0}".format(select5)
        if select6 != "Выбрать..":
            urlA += "&DDR={0}".format(select6)
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        print(urlA)
        print(temp)
        for ch in temp:
            if i >= 30:
                break
            try:
                proc = Operative.objects.get(id=int(ch))
                list.append(proc)
                i+=1
            except Exception:
                t = ""
        urlA = "https://checklistday.000webhostapp.com/api/videocard?name="
        urlA += urllib.parse.quote(ser)
        if select != "Выбрать..":
            urlA += "&GPU="
            urlA += urllib.parse.quote(select)
        if select2 != "Выбрать..":
            urlA += "&memory_to={0}&&memory_from={0}".format(select2)
        print(urlA)
        url = urllib.request.urlopen(urlA)
        temp = json.loads(url.read().decode())
        print(temp)
        for ch in temp:
            if i >= 30:
                break
            try:
                proc = Videocard.objects.get(id=int(ch))
                list.append(proc)
                i += 1
            except Exception:
                t = 1
    else:
        if list1 == '1':
            urlA = "https://checklistday.000webhostapp.com/api/processor?name="
            urlA += urllib.parse.quote(ser)
            if select7 != "Выбрать..":
                urlA += "&socket={0}".format(select7)
            if select8 != "Выбрать..":
                urlA += "&cores_from={0}&cores_to={0}".format(select8)
            url = urllib.request.urlopen(urlA)
            temp = json.loads(url.read().decode())
            print(temp)
            for ch in temp:
                if i >= 30:
                    break
                try:
                    proc = Proc.objects.get(id=int(ch))
                    list.append(proc)
                    i += 1
                except Exception:
                    t = 1
        if list2 == '1':
            urlA = "https://checklistday.000webhostapp.com/api/videocard?name="
            urlA += urllib.parse.quote(ser)
            if select != "Выбрать..":
                urlA += "&GPU="
                urlA += urllib.parse.quote(select)
            if select2 != "Выбрать..":
                urlA += "&memory_to={0}&memory_from={0}".format(select2)
            url = urllib.request.urlopen(urlA)
            temp = json.loads(url.read().decode())
            print(temp)
            for ch in temp:
                if i >= 30:
                    break
                try:
                    proc = Videocard.objects.get(id=int(ch))
                    list.append(proc)
                    i += 1
                except Exception:
                    t = ""
            print(list.__len__())
        if list3 == '1':
            print("operativa")
            urlA = "https://checklistday.000webhostapp.com/api/operative?name="
            urlA += urllib.parse.quote(ser)
            if select5 != "Выбрать..":
                urlA += "&v_to={0}&v_from={0}".format(select5)
            if select6 != "Выбрать..":
                urlA += "&DDR={0}".format(select6)
            url = urllib.request.urlopen(urlA)
            temp = json.loads(url.read().decode())
            print(temp)
            for ch in temp:
                if i >= 30:
                    break
                try:
                    i += 1
                    proc = Operative.objects.get(id=int(ch))
                    list.append(proc)
                except Exception:
                    t = ""
            print(list.__len__())
        if list4 == '1':
            urlA = "https://checklistday.000webhostapp.com/api/mother?name="
            urlA += urllib.parse.quote(ser)
            if select3 != "Выбрать..":
                urlA += "&form_factor={0}".format(select3)
            if select4 != "Выбрать..":
                urlA += "&proc_socket={0}".format(select4)
            url = urllib.request.urlopen(urlA)
            temp = json.loads(url.read().decode())
            print(urlA)
            print(temp)
            for ch in temp:
                if i >= 30:
                    break
                try:
                    proc = Motherboard.objects.get(id=int(ch))
                    list.append(proc)
                    i += 1
                except Exception:
                    t = 1
    count = list.__len__()
    print(count)
    return render(request1, 'tovar/index.html', {'gl': 12, 'ser': ser, 'temp': list, 'count': count, 'list1': list1, 'list2': list2, 'list3': list3, 'list4': list4})


def buy(request1):
    print("buy")
    name = request1.GET.get('id')
    min_max = request1.GET.get('minORmax')
    print(name)
    gam = games.objects.get(name=name)
    print(gam.json_min)
    if min_max == 0:
        json_min = json.loads(gam.json_min)
    else:
        json_min = json.loads(gam.json_max)
    RAM = json_min['RAM']
    proc = json_min['proc']
    mother = json_min['mother']
    videocard = json_min['videocard']
    ram_min = Operative.objects.get(id=int(RAM))
    proc_min = Proc.objects.get(id=int(proc))
    mother_min = Motherboard.objects.get(id=int(mother))
    videocard_min = Videocard.objects.get(id=int(videocard))
    print(videocard_min)
    if auth.get_user(request1).username.__len__() > 0:
        pr = Profile.objects.get(user=User.objects.get(username=auth.get_user(request1).username))
        sum = proc_min.min_price + mother_min.min_price + videocard_min.min_price + ram_min.min_price
        bd = buyed(profile=pr, price=sum, proc=proc_min, mother=mother_min, video=videocard_min, operative=ram_min,
                   json=json, name=name)
        bd.save()

    else:
        return render(request1, 'tovar/index.html', {'gl': 9})
    return render(request1, 'tovar/index.html', {'username': pr.user.username, 'gl': 1})


def src(request1):
    name = request1.GET.get('ser')
    print(name)
    try:
        game = games.objects.get(name__istartswith=name)
    except Exception:
        return HttpResponse("no")
    print(game.name)
    auth1 = ""
    if auth.get_user(request1).username.__len__() > 0:
        auth1 = auth.get_user(request1).username
        auth1 = auth1[:10]
    json_min = json.loads(game.json_min)
    json_max = json.loads(game.json_max)
    print(json_min)
    print(json_max)
    RAM = json_min['RAM']
    RAM2 = json_max['RAM']
    proc = json_min['proc']
    proc2 = json_max['proc']
    mother = json_min['mother']
    mother2 = json_max['mother']
    videocard = json_min['videocard']
    videocard2 = json_max['videocard']
    ram_min = Operative.objects.get(id=int(RAM))
    ram_max = Operative.objects.get(id=int(RAM2))
    proc_min = Proc.objects.get(id=int(proc))
    proc_max = Proc.objects.get(id=int(proc2))
    mother_min = Motherboard.objects.get(id=int(mother))
    mother_max = Motherboard.objects.get(id=int(mother2))
    videocard_min = Videocard.objects.get(id=int(videocard))
    videocard_max = Videocard.objects.get(id=int(videocard2))
    print(ram_min.name)
    min_price = ram_min.min_price + mother_min.min_price + videocard_min.min_price
    min_price2 = ram_max.min_price + mother_max.min_price + videocard_max.min_price
    return render(request1, 'tovar/index.html',
                  {'username': auth1, 'gl': 5, 'game': game, 'ram_min': ram_min, 'ram_max': ram_max,
                   'proc_min': proc_min, 'proc_max': proc_max, 'mother_min': mother_min, 'mother_max': mother_max,
                   'videocard_min': videocard_min, 'videocard_max': videocard_max, 'min_price': min_price,
                   'min_price2': min_price2})


def select(request1):
    print("select")
    name = request1.GET.get('id')
    game = games.objects.get(name=name)
    print(game.name)
    auth1 = ""
    if auth.get_user(request1).username.__len__() > 0:
        auth1 = auth.get_user(request1).username
        auth1 = auth1[:10]
    json_min = json.loads(game.json_min)
    json_max = json.loads(game.json_max)
    print(json_min)
    print(json_max)
    RAM = json_min['RAM']
    RAM2 = json_max['RAM']
    proc = json_min['proc']
    proc2 = json_max['proc']
    mother = json_min['mother']
    mother2 = json_max['mother']
    videocard = json_min['videocard']
    videocard2 = json_max['videocard']
    ram_min = Operative.objects.get(id=int(RAM))
    ram_max = Operative.objects.get(id=int(RAM2))
    proc_min = Proc.objects.get(id=int(proc))
    proc_max = Proc.objects.get(id=int(proc2))
    mother_min = Motherboard.objects.get(id=int(mother))
    mother_max = Motherboard.objects.get(id=int(mother2))
    videocard_min = Videocard.objects.get(id=int(videocard))
    videocard_max = Videocard.objects.get(id=int(videocard2))
    print(ram_min.name)
    min_price = ram_min.min_price + mother_min.min_price + videocard_min.min_price
    min_price2 = ram_max.min_price + mother_max.min_price + videocard_max.min_price
    return render(request1, 'tovar/index.html',
                  {'username': auth1, 'gl': 5, 'game': game, 'ram_min': ram_min, 'ram_max': ram_max,
                   'proc_min': proc_min, 'proc_max': proc_max, 'mother_min': mother_min, 'mother_max': mother_max,
                   'videocard_min': videocard_min, 'videocard_max': videocard_max, 'min_price': min_price,
                   'min_price2': min_price2})


def logout(request1):
    auth.logout(request1)
    return redirect("/")


def profile(request1):
    print("ПРофиль")
    if auth.get_user(request1).username.__len__() > 0:
        auth1 = auth.get_user(request1).username
        auth1 = auth1[:10]
    pr = Profile.objects.get(user=User.objects.get(username=auth.get_user(request1).username))
    bd = buyed.objects.filter(profile=pr)
    return render(request1, 'tovar/index.html', {'username': auth1, 'gl': 4, 'bd': bd})


def reg(request1):
    print("Регистрация")
    return render(request1, 'tovar/index.html', {'gl': 2})


def register(request):
    newuser_form = UserCreationForm(request.GET)
    if newuser_form.is_valid():
        newuser_form.save()
        newuser = authenticate(username=request.GET.get('username'), password=request.GET.get('password1'))
        print(newuser)
        login(request, newuser)
        return HttpResponse('yea', content_type='text/html')
    else:
        return HttpResponse(newuser_form.errors, content_type='text/html')


def Tologin(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        auth1 = username[:10]
        return HttpResponse('yea', content_type='text/html')
    else:
        return HttpResponse('non', content_type='text/html')


def vhod(request1):
    print("Вход")
    return render(request1, 'tovar/index.html', {'gl': 3})


def podbor(request1):
    print("games")
    auth1 = ""
    if auth.get_user(request1).username.__len__() > 0:
        auth1 = auth.get_user(request1).username
        auth1 = auth1[:10]
    gam = games.objects.all()
    return render(request1, 'tovar/index.html', {'username': auth1, 'gl': 0, 'gam': gam})


def main(request1):
    print("3")
    auth1 = ""
    if auth.get_user(request1).username.__len__() > 0:
        auth1 = auth.get_user(request1).username
        auth1 = auth1[:10]
    return render(request1, 'tovar/index.html', {'username': auth1, 'gl': 1})
