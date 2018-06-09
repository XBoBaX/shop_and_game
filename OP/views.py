from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
import requests, time, re
from .models import Operative, Price
from videokarta.models import Connection
from proccesor.models import Soket


def get_pr(pr1, i, href, price):
    pr = Operative.objects.filter(name=pr1).first()
    try:
        price_list = Price.objects.get(tovar=pr)
    except Exception:
        price_list = Price(tovar=pr)
    i_t = 0
    if price_list.adress1 == None or price_list.adress1 == "":
        price_list.adress1 = href
        price_list.price1 = price
        i_t = 1
    elif price_list.adress2 == None or price_list.adress2 == "":
        price_list.adress2 = href
        price_list.price2 = price
        i_t = 2
    elif price_list.adress3 == None or price_list.adress3 == "":
        price_list.adress3 = href
        price_list.price3 = price
        i_t = 3
    elif price_list.adress4 == None or price_list.adress4 == "":
        price_list.adress4 = href
        price_list.price4 = price
        i_t = 4
    elif price_list.adress5 == None or price_list.adress5 == "":
        price_list.adress5 = href
        price_list.price5 = price
        i_t = 5
    elif price_list.adress6 == None or price_list.adress6 == "":
        price_list.adress6 = href
        price_list.price6 = price
        i_t = 6
    elif price_list.adress7 == None or price_list.adress7 == "":
        price_list.adress7 = href
        price_list.price7 = price
        i_t = 7
    elif price_list.adress8 == None or price_list.adress8 == "":
        price_list.adress8 = href
        price_list.price8 = price
        i_t = 8
    elif price_list.adress9 == None or price_list.adress9 == "":
        price_list.adress9 = href
        price_list.price9 = price
        i_t = 9
    elif price_list.adress10 == None or price_list.adress10 == "":
        price_list.adress10 = href
        price_list.price10 = price
        i_t = 10

    price_list.save()
    print("{0}){1} Сохранен".format(i_t, pr))


def price(request):
    print("hello2")
    proc = Operative.objects.all()
    for pr1 in proc:
        pr = pr1.name.replace('Оперативная память', '')
        # url_html = get_url("https://repka.ua/catalogsearch/result/?q={0}".format(pr))
        # i = 0
        # try:
        #     li_list = soup_price(url_html)
        #     for li in li_list:
        #         pr_shor = pr[pr.find('[') + 1:pr.find(']')]
        #         if li.find('a', class_="name").getText().find(pr_shor) != -1:
        #             href = li.find('a')['href']
        #             price = li.find('span', class_="price").getText()
        #             price = int(price.replace('грн', '').replace(' ', '').replace(' ', ''))
        #             print(price)
        #             print(li.find('a')['href'])
        #
        #             get_pr(pr1.name, i, href, price)
        #
        #             i += 1
        #             break
        # except:
        #     print("В репке нет: {0}".format(pr1.name))

        # url_html = get_url("https://eldorado.ua/search?q={0}".format(pr))
        # i = 0
        # try:
        #     li_list = soup_price_2(url_html)
        #     for li in li_list:
        #         href = li.find('div', class_="title lp").find('a')['href']
        #         href = "https://eldorado.ua{0}".format(href)
        #         try:
        #             price = li.find('div', class_="current-price h1").getText()
        #             price = int(price[:price.find(' ')])
        #         except:
        #             price = 0
        #         print(pr1.name)
        #         print(href)
        #         print(price)
        #         get_pr(pr1.name, i, href, price)
        #         i += 1
        #         break
        # except Exception:
        #     print("В магазине Eldarado нет товара: {0}".format(pr))

        # pr_shor = pr[pr.find('[') + 1:pr.find(']')]
        # url_html = get_url("http://amain.com.ua/index.php?route=product/search&search={0}&filter_category_id=1578".format(pr_shor))
        # i = 0
        # try:
        #     li_list = soup_price_3(url_html)
        #     for li in li_list:
        #         a = li.find('a', class_="product-title to-left color-black")
        #         if a == None:
        #             continue
        #         if li.find('a', class_="product-title to-left color-black").getText().find(pr_shor) != -1:
        #             href = li.find('a', 'product-title to-left color-black')['href']
        #             try:
        #                 price = li.find('p', class_="price color-orange").getText()
        #                 price = int(price.replace('грн', '').replace(' ', '').replace(' ', ''))
        #             except Exception:
        #                 price = 0
        #             print(pr1.name)
        #             print(href)
        #             print(price)
        #             get_pr(pr1.name, i, href, price)
        #             i += 1
        #             break
        # except Exception:
        #     print("В магазине amain нет товара: {0}".format(pr))

        # pr_shor = pr[pr.find('[') + 1:pr.find(']')]
        # url_html = get_url("https://telemart.ua/search/?search_que={0}&id_category=403".format(pr_shor))
        # i = 0
        # try:
        #     li_list = soup_price_4(url_html)
        #     for li in li_list:
        #         a = li.find('a')
        #         if a == None:
        #             continue
        #         href = li.find('a')['href']
        #         try:
        #             price = li.find('div', class_="b-price").getText()
        #             price = int(price.replace('грн', '').replace(' ', '').replace(' ', ''))
        #         except Exception:
        #             price = 0
        #         print(pr1.name)
        #         print(href)
        #         print(price)
        #         get_pr(pr1.name, i, href, price)
        #         i += 1
        #         break
        # except Exception:
        #     print("В магазине allo нет товара: {0}".format(pr))
        # pr_shor = pr[pr.find('[') + 1:pr.find(']')]
        # url_html = get_url("http://57.kharkov.ua/search?title={0}&term_node_tid_depth=All".format(pr_shor))
        # i = 0
        # try:
        #     li_list = soup_price_5(url_html)
        #     # print(li_list)
        #     for li in li_list:
        #         a = li.find('div', class_="views-field-title").find('a')
        #         if a == None:
        #             continue
        #         href = "57.kharkov.ua{0}".format(li.find('div', class_="views-field-title").find('a')['href'])
        #         try:
        #             price = li.find('div', 'sell-price').getText()
        #             price = int(price.replace('грн.', '').replace(' ', '').replace(' ', ''))
        #         except Exception:
        #             price = 0
        #         print(pr1.name)
        #         print(href)
        #         print(price)
        #         get_pr(pr1.name, i, href, price)
        #         i += 1
        #         break
        # except Exception:
        #     print("В магазине fallo нет товара: {0}".format(pr))
    price_1 = Price.objects.all()
    for price_list in price_1:
        sm = []
        adress = []
        if price_list.adress1 != None and price_list.adress1 != "":
            sm.append(price_list.price1)
            adress.append(price_list.adress1)
            i_t = 1
        if price_list.adress2 != None and price_list.adress2 != "":
            sm.append(price_list.price2)
            adress.append(price_list.adress2)
            i_t = 2
        if price_list.adress3 != None and price_list.adress3 != "":
            adress.append(price_list.adress3)
            sm.append(price_list.price3)
            i_t = 3
        if price_list.adress4 != None and price_list.adress4 != "":
            i_t = 4
            adress.append(price_list.adress4)
            sm.append(price_list.price4)
        if price_list.adress5 != None and price_list.adress5 != "":
            adress.append(price_list.adress5)
            i_t = 5
            sm.append(price_list.price5)
        if price_list.adress6 != None and price_list.adress6 != "":
            adress.append(price_list.adress6)
            i_t = 6
            sm.append(price_list.price6)
        if price_list.adress7 != None and price_list.adress7 != "":
            adress.append(price_list.adress7)
            i_t = 7
            sm.append(price_list.price7)
        if price_list.adress8 != None and price_list.adress8 != "":
            adress.append(price_list.adress8)
            i_t = 8
            sm.append(price_list.price8)
        if price_list.adress9 != None and price_list.adress9 != "":
            adress.append(price_list.adress9)
            i_t = 9
            sm.append(price_list.price9)
        if price_list.adress10 != None and price_list.adress10 != "":
            adress.append(price_list.adress10)
            i_t = 10
            sm.append(price_list.price10)
        ji = 0
        min = sm[0]
        adr = price_list.adress1
        for ch in sm:
            print(ch)
            if ch != 0:
                if ch < min:
                    min = ch
                    adr = adress[ji]
            ji += 1
        price_list.count = i_t
        prr = price_list.tovar
        prr.min_price = min
        prr.min_price_ad = adr
        price_list.save()
        prr.save()
        print("money: {0}".format(min))
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def soup_price_5(html):
    temp = BeautifulSoup(html, 'lxml').find('div', class_="item-list").find_all('li')
    # print(html)
    return temp

def soup_price_4(html):
    temp = BeautifulSoup(html, 'lxml').find_all('div', class_="b-i-product product_wrapper ")
    # print(temp)
    return temp

def soup_price_3(html):
    temp = BeautifulSoup(html, 'lxml').find_all('div', class_="white-block")
    return temp


def soup_price_2(html):
    temp = BeautifulSoup(html, 'lxml').find_all('div', class_="goods-item false")
    return temp

def soup_price(html):
    temp = BeautifulSoup(html, 'lxml').find_all('li', class_="item product product-item")
    return temp


def update(request):
    print("hello1")
    url_html = get_url("http://ek.ua/list/188/")
    temp_soup = BeautifulSoup(url_html, 'lxml').find('div', class_="ib page-num").find_all('a')
    max = temp_soup[-1].getText()
    print(max)
    ind = 1
    while ind < int(max) - 1:
        if ind != 0:
            try:
                url_html = get_url("http://ek.ua/list/188/{0}/".format(ind))
            except Exception:
                continue
        # форма и пагинация
        a = parsing(url_html)
        for href in a:
            ss = href['href']
            url_html = get_url("http://ek.ua/{0}".format(ss))
            soup = BeautifulSoup(url_html, 'lxml')
            name = soup.find('div', id="top-page-title").find('h1', class_="t2").getText()
            print(name)
            soup = soup.find('table', class_="one-col")
            mas = ['Объем памяти', 'Кол-во планок в', 'Форм-фактор', 'Тип', 'Тактовая',
                   'Пропускная', 'охлаждения']
            op = Operative(name=name)
            print("_______________")
            for ch in mas:
                try:
                    temp = soup.find(text=re.compile(r'{0}'.format(ch))).parent.parent.parent
                except Exception:
                    continue
                if temp.find('td', class_="val"):
                    t = ""
                else:
                    temp = temp.parent
                try:
                    xar = temp.find('td', class_="val").getText()
                except Exception:
                    continue
                print(xar)
                if ch == "Объем памяти":
                    op.V_eto_obem = xar
                elif ch == "Кол-во планок в":
                    op.count_comp = xar
                elif ch == "Форм-фактор":
                    op.DIMM = xar
                elif ch == "Тип":
                    op.DDR = xar
                elif ch == "Тактовая":
                    op.freq = xar
                elif ch == "охлаждения":
                    op.freq1 = xar
                elif ch == "Пропускная":
                    op.cooler = xar
                op.save()
        ind += 1


def get_url(url):
    kol = 0
    while kol < 3:
        try:
            url_html = get_html(url)
            kol = 3
        except Exception:
            kol += 1
            time.sleep(kol)
    return url_html


def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def pars_proc(html):
    soup = BeautifulSoup(html, 'lxml')
    list_temp = soup.find('div', id='conf_item_descr')
    return list_temp


def parsing(html):
    soup = BeautifulSoup(html, 'lxml')
    list_temp = soup.find_all('a', class_='conf-name')
    return list_temp
