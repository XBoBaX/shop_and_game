from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
import requests, time, re
from .models import Soket, Proc, Price


def get_pr(pr, i, href, price):
    pr = Proc.objects.get(name=pr)
    i_t = 0
    try:
        price_list = Price.objects.get(tovar=pr)
    except Exception:
        price_list = Price(tovar=pr)
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
    proc = Proc.objects.all()
    for pr1 in proc:
        pr = pr1.name.replace('Процессор ', '')

        # url_html = get_url("https://repka.ua/catalogsearch/result/?q={0}".format(pr))
        i = 0
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
        #         pr_shor = pr[pr.find('[') + 1:pr.find(']')]
        #         if li.find('div', class_="title lp").find('div').getText().find(pr_shor) != -1:
        #             href = li.find('div', class_="title lp").find('a')['href']
        #             href = "https://eldorado.ua{0}".format(href)
        #             price = li.find('div', class_="current-price h1").getText()
        #             price = int(price[:price.find(' ')])
        #             print(pr1.name)
        #             print(href)
        #             print(price)
        #             get_pr(pr1.name, i, href, price)
        #             i += 1
        #             break
        # except Exception:
        #     print("В магазине Eldarado нет товара: {0}".format(pr))
        # pr_shor = pr[pr.find('[') + 1:pr.find(']')]
        # url_html = get_url(
        #     "http://amain.com.ua/index.php?route=product/search&search={0}&filter_category_id=1579".format(pr_shor))
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
        # url_html = get_url("https://telemart.ua/search/?search_que={0}&id_category=398".format(pr_shor))
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
            # sm1 = price_list.price1
            i_t = 1
        if price_list.adress2 != None and price_list.adress2 != "":
            # sm2 = price_list.price2
            sm.append(price_list.price2)
            adress.append(price_list.adress2)

            i_t = 2
        if price_list.adress3 != None and price_list.adress3 != "":
            # sm3 = price_list.price3
            adress.append(price_list.adress3)
            sm.append(price_list.price3)
            i_t = 3
        if price_list.adress4 != None and price_list.adress4 != "":
            # sm4 = price_list.price4
            i_t = 4
            adress.append(price_list.adress4)
            sm.append(price_list.price4)
        if price_list.adress5 != None and price_list.adress5 != "":
            # sm5 = price_list.price5
            adress.append(price_list.adress5)
            i_t = 5
            sm.append(price_list.price5)
        if price_list.adress6 != None and price_list.adress6 != "":
            # sm6 = price_list.price6
            adress.append(price_list.adress6)
            i_t = 6
            sm.append(price_list.price6)
        if price_list.adress7 != None and price_list.adress7 != "":
            # sm7 = price_list.price7
            adress.append(price_list.adress7)
            i_t = 7
            sm.append(price_list.price7)
        if price_list.adress8 != None and price_list.adress8 != "":
            # sm8 = price_list.price8
            adress.append(price_list.adress8)
            i_t = 8
            sm.append(price_list.price8)
        if price_list.adress9 != None and price_list.adress9 != "":
            # sm9 = price_list.price9
            adress.append(price_list.adress9)
            i_t = 9
            sm.append(price_list.price9)
        if price_list.adress10 != None and price_list.adress10 != "":
            # sm10 = price_list.price10
            adress.append(price_list.adress10)

            i_t = 10
            sm.append(price_list.price10)
        # print("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(sm1, sm2, sm3, sm4, sm5, sm6, sm7, sm8, sm9,
        #                                                                 sm10))
        # print(i_t)
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


def soup_price(html):
    temp = BeautifulSoup(html, 'lxml').find_all('li', class_="item product product-item")
    return temp


def soup_price_2(html):
    temp = BeautifulSoup(html, 'lxml').find_all('div', class_="goods-item false")
    return temp


def soup_price_3(html):
    temp = BeautifulSoup(html, 'lxml').find_all('div', class_="white-block")
    return temp


def update(request):
    print("hello1")
    url_html = get_url("http://ek.ua/list/186/")

    temp_soup = BeautifulSoup(url_html, 'lxml').find('div', class_="ib page-num").find_all('a')
    ind = 0
    for i in temp_soup:
        if ind != 0:
            url_html = get_url("http://ek.ua/list/186/{0}/".format(ind))
        ind += 1
        # форма и пагинация
        main_page = parsing(url_html)
        # форма
        table = main_page.find('form').find_all('table', class_="conf-table")
        for tr in table:
            mas = ['Socket', 'Серия', 'Кол-во', 'Тактовая', 'GPU',
                   'Частота TurboBoost /', 'Техпроцесс', 'Архитектура',
                   '1-го уровня', '2-го уровня', '3-го уровня', 'Тепловыделение',
                   'инструкций', 'объем', 'Макс. частота']
            a_link = tr.find_all('a', class_="conf-name")
            for href in a_link:
                html = get_url("http://ek.ua{0}".format(href['href']))
                charact = pars_proc(html)
                table_list = charact.find_all('table', id="help_table")
                kyller = int_vid = False
                mas_to = []
                for tr_hl in table_list:
                    print("_______")
                    temp = tr_hl.find(text=re.compile(r'Комплектуется кулером'))
                    if temp != None:
                        par = temp.parent.parent.parent.parent
                        img = par.find('img')
                        if img['src'] == "/img/icons/bul_141.gif":
                            kyller = True
                    temp = tr_hl.find(text=re.compile(r'Интегрированная графика'))
                    if temp != None:
                        par = temp.parent.parent.parent.parent
                        img = par.find('img')
                        if img['src'] == "/img/icons/bul_141.gif":
                            kyller = True
                    name = BeautifulSoup(html, 'lxml').find('div', id="top-page-title").find('h1',
                                                                                             class_="t2").getText()
                    print("Процессор) {0}".format(name))
                    print("Комплектуется кулером) {0}".format(kyller))
                    print("Интегрированная графика) {0}".format(int_vid))
                    for ch in mas:
                        temp = tr_hl.find(text=re.compile(r"{0}".format(ch)))
                        if temp != None:
                            par = temp.parent.parent.parent
                            if par.find('td', class_="op3"):
                                t = ""
                            else:
                                par = par.parent
                            try:
                                xar = par.find('td', class_="op3").getText()
                            except Exception:
                                continue
                            if ch == "Socket":
                                try:
                                    sk = Soket.objects.get(name=xar)
                                    pr1 = Proc(name=name, cooler=kyller, integer_video=int_vid, sok=sk)
                                except Exception:
                                    sk = Soket(name=xar)
                                    sk.save()
                                    pr1 = Proc(name=name, cooler=kyller, integer_video=int_vid, sok=sk)
                                print(sk)
                            print("{0}) {1}".format(ch, xar))
                            if ch == 'Серия':
                                pr1.series = xar
                            elif ch == "Кол-во":
                                pr1.count_core = xar
                            elif ch == "Тактовая":
                                pr1.clock_freq = xar
                            elif ch == "GPU":
                                pr1.model_GPU = xar
                            elif ch == "Частота TurboBoost /":
                                pr1.freq = xar
                            elif ch == "Техпроцесс":
                                pr1.proc_tech = xar
                            elif ch == "Архитектура":
                                pr1.architecture = xar
                            elif ch == "1-го уровня":
                                pr1.L1 = xar
                            elif ch == "2-го уровня":
                                pr1.L2 = xar
                            elif ch == "3-го уровня":
                                pr1.L3 = xar
                            elif ch == "Тепловыделение":
                                pr1.TDP = xar
                            elif ch == "инструкций":
                                pr1.sup_instr = xar
                            elif ch == "объем":
                                pr1.max_vol = xar
                            elif ch == "Макс. частота":
                                pr1.max_kanal = xar
                            pr1.save()
                            mas_to.append(xar)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


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
    list_temp = soup.find('td', class_='main-part-content')
    return list_temp
