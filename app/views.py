from django.http import HttpResponse
from django.shortcuts import render
from .forms import Client_ColorForm, Client_ColorForm_en, Client_ColorForm_es, Client_ColorForm_ar, Client_ColorForm_cz, \
    Client_ColorForm_ind, Client_ColorForm_gr, Client_ColorForm_fr, Client_ColorForm_ch, Client_ColorForm_kr, \
    Client_ColorForm_ic, Client_ColorForm_srb, Client_ColorForm_reg
from app.models import Client_Color1, Client_Color2
import datetime


def indexLn(request):
    msg = 'Когда вы заполните все поля анкеты, нажмите "продолжить" чтобы перейти к странице выбора цвета.'
    if request.method == "POST":
        form = Client_ColorForm(request.POST)
        if form.is_valid():
            client = form.save()  # commit=False)
            print(client.Client_sex)
            print(client.Client_edu)
            print(client.Client_Year)
            msg = client.Client_id
            # Set a session value:
            request.session["User_id"] = client.Client_id
            # добавила Самойлова 24.5.22
            key = client.Client_id
            current_user = Client_Color1.objects.get(pk=key)
            date = datetime.datetime.today()
            current_user.color1 = date.strftime("%m/%d/%Y, %H:%M:%S")
            current_user.save(update_fields=['color1'])
            # конец добавки
            Lg = request.session["Lg"]
            if Lg == "en":
                next = "CONTINUE"
            elif Lg == "es":
                next = "CONTINUAR"
            elif Lg == "ar":
                next = "متابعة"
            elif Lg == "cz":
                next = "POKRAČOVAT"
            elif Lg == "ind":
                next = "LANJUTKAN"
            elif Lg == "gr":
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                next = "Continuer"
            elif Lg == "ch":
                next = "繼續"
            elif Lg == "kr":
                next = "계속"
            elif Lg == "ic":
                next = "Halda áfram"
            elif Lg == "srb":
                next = "DALJE"
            else:
                next = "ПРОДОЛЖИТЬ"
            return render(request, 'index1.html', {'message': msg, 'Lg': Lg, 'next': next})

        else:
            if request.POST['language'] == 'ru':
                form = Client_ColorForm()
                request.session["Lg"] = 'ru'
                Lg = 'ru'
                next = "ПРОДОЛЖИТЬ"
                msg = 'Когда вы заполните все поля анкеты, нажмите "продолжить" чтобы перейти к странице выбора цвета.'
            elif request.POST['language'] == 'es':
                form = Client_ColorForm_es()
                request.session["Lg"] = 'es'
                Lg = 'es'
                next = "CONTINUAR"
                msg = 'Después de haber respondido todas las preguntas, clickea "continuar" para ir a la página de selección de colores.'
            elif request.POST['language'] == 'ar':
                form = Client_ColorForm_ar()
                request.session["Lg"] = 'ar'
                Lg = 'ar'
                next = "متابعة"
                msg = 'بعد إجابتك مشكورا على كامل البيانات المطلوبة ، إضغط على الزر "متابعة" للإنتقال إلى صفحة اختيار الألوان'
            elif request.POST['language'] == 'cz':
                form = Client_ColorForm_cz()
                request.session["Lg"] = 'cz'
                Lg = 'cz'
                next = "POKRAČOVAT"
                msg = 'Po vyplnění všech polí klikněte na "pokračovat" a přejděte na stránku pro výběr barvy.'
            elif request.POST['language'] == 'ind':
                form = Client_ColorForm_ind()
                request.session["Lg"] = 'ind'
                Lg = 'ind'
                next = "LANJUTKAN"
                msg = 'Setelah Anda menjawab semua pertanyaan, klik "lanjutkan" untuk masuk ke halaman pemilihan warna.'
            elif request.POST['language'] == 'gr':
                form = Client_ColorForm_gr()
                request.session["Lg"] = 'gr'
                Lg = 'gr'
                next = "ΣΥΝΕΧΕΙΑ"
                msg = 'Αφού απαντήσετε όλες τις ερωτήσεις, πατήστε "συνέχεια" για να πάτε στη σελίδα με την επιλογή χρώματος.'
            elif request.POST['language'] == 'fr':
                form = Client_ColorForm_fr()
                request.session["Lg"] = 'fr'
                Lg = 'fr'
                next = "Continuer"
                msg = 'Après avoir répondu à toutes les questions, cliquez sur « continuer » pour accéder à la page de sélection des couleurs.'
            elif request.POST['language'] == 'ch':
                form = Client_ColorForm_ch()
                request.session["Lg"] = 'ch'
                Lg = 'ch'
                next = "繼續"
                msg = '回答所有問題後，請點擊“繼續continue”進入選色頁面。'
            elif request.POST['language'] == 'kr':
                form = Client_ColorForm_kr()
                request.session["Lg"] = 'kr'
                Lg = 'kr'
                next = "계속"
                msg = '모든 질문에 답한 후 "계속"을 클릭하여 색상 선택 페이지로 이동하세요.'
            elif request.POST['language'] == 'ic':
                form = Client_ColorForm_ic()
                request.session["Lg"] = 'ic'
                Lg = 'ic'
                next = "Halda áfram"
                msg = 'Smelltu á "Halda áfram" til að hefja litarannsóknina, þegar þú hefur lokið við að svara spurningunum.'
            elif request.POST['language'] == 'srb':
                form = Client_ColorForm_srb()
                request.session["Lg"] = 'srb'
                Lg = 'srb'
                next = "DALJE"
                msg = 'Nakon što ste odgovorili na sva pitanja, kliknite na dugme DALJE da pređete na stranicu gde se biraju boje.'
            else:
                form = Client_ColorForm_en()
                request.session["Lg"] = 'en'
                Lg = 'en'
                next = "CONTINUE"
                msg = 'After you have answered all the questions, click "continue" to go to the color selection page.'
            return render(request, 'index.html', {'form': form, 'message': msg, 'Lg': Lg, 'next': next})
    else:
        form = Client_ColorForm_en()
        request.session["Lg"] = "en"
        Lg = "en"
        next = "CONTINUE"
        msg = 'After you have answered all the questions, click "continue" to go to the color selection page.'
    return render(request, 'index.html', {'form': form, 'message': msg, 'Lg': Lg, 'next': next})


def index(request):
    msg = 'Когда вы заполните все поля анкеты, нажмите "продолжить" чтобы перейти к странице выбора цвета.'
    if request.method == "POST":
        form = Client_ColorForm_en(request.POST)
        if form.is_valid():
            client = form.save()  # commit=False)
            print(client.Client_sex)
            print(client.Client_edu)
            print(client.Client_Year)
            msg = client.Client_id
            # Set a session value:
            request.session["User_id"] = client.Client_id
            # добавила Самойлова 24.5.22
            key = client.Client_id
            current_user = Client_Color1.objects.get(pk=key)
            date = datetime.datetime.today()
            current_user.color1 = date.strftime("%m/%d/%Y, %H:%M:%S")
            current_user.save(update_fields=['color1'])
            # конец добавки
            Lg = "en"
            next = "CONTINUE"
            return render(request, 'index1.html', {'form': form, 'message': msg, 'Lg': Lg, 'next': next})
    else:
        form = Client_ColorForm_en()
        request.session["Lg"] = "en"
        Lg = "en"
        next = "CONTINUE"
        msg = 'After you have answered all the questions, click "continue" to go to the color selection page.'
    return render(request, 'index.html', {'form': form, 'message': msg, 'Lg': Lg, 'next': next})


def index1(request):
    msg = "Все хорошо"
    if request.method == "POST":
        MyColor = request.POST['mycolor']
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.color1.strip('/')  # вставила  самойлова 28.5.22
        if (s[0] == '#'):  # вставила  самойлова 28.5.22
            s = s[8:16]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.color1 = MyColor + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['color1'])  # изменила самойлова 24.5.22
        print(current_user.color1)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.color2 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['color2'])
        print(current_user.color2)
        # конец добавки
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index2.html', {'message': msg, 'Lg': Lg, 'next': next})
    else:
        msg = "Плохие данные"
        print(msg)
    return render(request, 'index1.html')


def index2(request):
    msg = "Все хорошо"
    if request.method == "POST":
        MyColor = request.POST['mycolor']
        key = request.session["User_id"]
        # current_user = Client_Color1.objects.all().order_by('-Client_id')[:1] [0]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.color2.strip('/')  # вставила  самойлова 28.5.22
        if (s[0] == '#'):  # вставила  самойлова 28.5.22
            s = s[8:16]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.color2 = MyColor + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['color2'])  # изменила самойлова 24.5.22
        print(current_user.color2)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.color3 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['color3'])
        print(current_user.color3)
        # конец добавки
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index3.html', {'message': msg, 'Lg': Lg, 'next': next})
    else:
        msg = "Плохие данные"
        print(msg)
    return render(request, 'index2.html')


def index3(request):
    msg = "Все хорошо"
    if request.method == "POST":
        MyColor = request.POST['mycolor']
        key = request.session["User_id"]
        # current_user = Client_Color1.objects.all().order_by('-Client_id')[:1] [0]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.color3.strip('/')  # вставила  самойлова 28.5.22
        if (s[0] == '#'):  # вставила  самойлова 28.5.22
            s = s[8:16]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.color3 = MyColor + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['color3'])  # изменила самойлова 24.5.22
        print(current_user.color3)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.color4 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['color4'])
        print(current_user.color4)
        # конец добавки
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index4.html', {'message': msg, 'Lg': Lg, 'next': next})
    else:
        msg = "Плохие данные"
        print(msg)
    return render(request, 'index3.html')


def index4(request):
    msg = "Все хорошо"
    if request.method == "POST":
        MyColor = request.POST['mycolor']
        key = request.session["User_id"]
        # current_user = Client_Color1.objects.all().order_by('-Client_id')[:1] [0]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.color4.strip('/')  # вставила  самойлова 28.5.22
        if (s[0] == '#'):  # вставила  самойлова 28.5.22
            s = s[8:16]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.color4 = MyColor + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['color4'])  # изменила самойлова 24.5.22
        print(current_user.color4)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.color5 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['color5'])
        print(current_user.color5)
        # конец добавки
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index5.html', {'message': msg, 'Lg': Lg, 'next': next})
    else:
        msg = "Плохие данные"
        print(msg)
    return render(request, 'index4.html')


def index5(request):
    msg = "Все хорошою. Перехожу на стр.6"
    if request.method == "POST":
        MyColor = request.POST['mycolor']
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.color5.strip('/')  # вставила  самойлова 28.5.22
        if (s[0] == '#'):  # вставила  самойлова 28.5.22
            s = s[8:16]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.color5 = MyColor + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['color5'])  # изменила самойлова 24.5.22
        print(current_user.color5)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left1 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left1'])
        print(current_user.left1)
        # конец добавки
        print(msg)
        msg = "начальный запуск страницы 6. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color1
        print(msg)
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index6.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "Плохие данные"
        print(msg)
    print('Первый запуск страницы 5')
    return render(request, 'index5.html')


def index6(request):
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            print(myleft)
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color1  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            print('Отладка2:MyColor = ', MyColor)
            return render(request, 'index6.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left1.strip('/')  # вставила  самойлова 28.5.22
        print('отладка s =', s)
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
            print('ОТЛАДКА if s = ', s)
        current_user.left1 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        print('отладка s =', s)
        current_user.save(update_fields=['left1'])  # изменила самойлова 24.5.22
        msg = "начальный запуск страницы 7. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color2
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left2 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left2'])
        print(current_user.left2)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index7.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index6.html')


def index7(request):  # СТРАНИЦА 2 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color2  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index7.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left2.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left2 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left2'])
        msg = "начальный запуск страницы 8. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color3
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left3 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left3'])
        print(current_user.left3)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index8.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index7.html')


def index8(request):  # СТРАНИЦА 3 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color3  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index8.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left3.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left3 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left3'])
        msg = "начальный запуск страницы 9. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color4
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left4 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left4'])
        print(current_user.left4)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index9.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index8.html')


def index9(request):  # СТРАНИЦА 4 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color4  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index9.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left4.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left4 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left4'])
        msg = "начальный запуск страницы 10. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color4
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left5 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left5'])
        print(current_user.left5)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index10.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index9.html')


def index10(request):  # СТРАНИЦА 5 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color4  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index10.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left5.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left5 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left5'])
        msg = "начальный запуск страницы 11. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color4
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left6 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left6'])
        print(current_user.left6)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index11.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index10.html')


def index11(request):  # СТРАНИЦА 6 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color4  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index11.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left6.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left6 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left6'])
        msg = "начальный запуск страницы 12. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color4
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left7 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left7'])
        print(current_user.left7)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index12.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index11.html')


def index12(request):  # СТРАНИЦА 7 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color4  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index12.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left7.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left7 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left7'])
        msg = "начальный запуск страницы 13. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color5
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left8 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left8'])
        print(current_user.left8)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index13.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index12.html')


def index13(request):  # СТРАНИЦА 8 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color5  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index13.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left8.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left8 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left8'])
        msg = "начальный запуск страницы 14. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color5
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left9 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left9'])
        print(current_user.left9)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index14.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index13.html')


def index14(request):  # СТРАНИЦА 9 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color5  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index14.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left9.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left9 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left9'])
        msg = "начальный запуск страницы 15. Чтение указанногоцвета"
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        MyColor = current_user.color5
        print(MyColor)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left10 = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['left10'])
        print(current_user.left10)
        # конец добавки
        # Обрезать дату, оставить только 7 первых символо
        MyColor = MyColor[:7]  # изменила самойлова 24.5.22
        print(msg)
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'index15.html', {'MyColor': MyColor, 'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index14.html')


def index15(request):  # СТРАНИЦА 10 с двумя таблицами
    if request.method == "POST":
        if 'left' not in request.POST:
            myleft = "null"
            print('НЕ ПЕРЕДАЛА!!!')
            key = request.session["User_id"]  ##### 4.5.22
            current_user = Client_Color1.objects.get(pk=key)  ##### 4.5.22
            MyColor = current_user.color5  ##### 4.5.22
            Lg = request.session["Lg"]
            if Lg == "en":
                msg = "No option is selected. Select left or right"  ##### 4.5.22
                next = "CONTINUE"
            elif Lg == "es":
                msg = "No se selecciona ninguna opción. Seleccione la izquierda o la derecha."
                next = "CONTINUAR"
            elif Lg == "ar":
                msg = "لم يتم تحديد أي خيار . حدد اليسار أو اليمين"
                next = "متابعة"
            elif Lg == "cz":
                msg = "Není vybráno nic. Vyberte hodnotu levá nebo pravá."
                next = "POKRAČOVAT"
            elif Lg == "ind":
                msg = "Tidak ada opsi yang dipilih. Pilih kiri atau kanan."
                next = "LANJUTKAN"
            elif Lg == "gr":
                msg = "Δεν έχετε κάνει καμία επιλογή. Επιλέξτε αριστερά ή δεξιά."
                next = "ΣΥΝΕΧΕΙΑ"
            elif Lg == "fr":
                msg = "Aucune option n'est sélectionnée. Sélectionnez gauche ou droite."
                next = "Continuer"
            elif Lg == "ch":
                msg = "尚未選擇任何選項。請選擇左或右。"
                next = "繼續"
            elif Lg == "kr":
                msg = "옵션이 선택되지 않았습니다. 왼쪽 또는 오른쪽을 선택합니다."
                next = "계속"
            elif Lg == "ic":
                msg = "Ekkert valið. Veldu annað hvort vinstri eða hægri."
                next = "Halda áfram"
            elif Lg == "srb":
                msg = "Nijedna opcija nije izabrana. Izaberite levu ili desnu opciju."
                next = "DALJE"
            else:
                msg = "Ничего не выбрано. Выберите значение слева/справа"  ##### 4.5.22
                next = "ПРОДОЛЖИТЬ"
            MyColor = MyColor[:7]  # изменила самойлова 17:6:22
            return render(request, 'index15.html',
                          {'msg': msg, 'MyColor': MyColor, 'Lg': Lg, 'next': next})  ##### 4.5.22
        else:
            myleft = request.POST['left']
            print('ПЕРЕДАЛА!!!')
            print(myleft)
        key = request.session["User_id"]
        current_user = Client_Color1.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.left10.strip('/')  # вставила  самойлова 28.5.22
        if (s[4] == ':'):  # вставила  самойлова 28.5.22
            s = s[2:10]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.left10 = myleft + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['left10'])
        print('end')
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.left10 = current_user.left10.strip() + date.strftime('%H:%M:%S') + '/'
        current_user.save(update_fields=['left10'])
        print(current_user.left10)
        # конец добавки
        Lg = request.session["Lg"]
        if Lg == "en":
            next = "CONTINUE"
        elif Lg == "es":
            next = "CONTINUAR"
        elif Lg == "ar":
            next = "متابعة"
        elif Lg == "cz":
            next = "POKRAČOVAT"
        elif Lg == "ind":
            next = "LANJUTKAN"
        elif Lg == "gr":
            next = "ΣΥΝΕΧΕΙΑ"
        elif Lg == "fr":
            next = "Continuer"
        elif Lg == "ch":
            next = "繼續"
        elif Lg == "kr":
            next = "계속"
        elif Lg == "ic":
            next = "Halda áfram"
        elif Lg == "srb":
            next = "DALJE"
        else:
            next = "ПРОДОЛЖИТЬ"
        return render(request, 'indexend.html', {'Lg': Lg, 'next': next})
    else:
        msg = "kuku"
        print(msg)
    return render(request, 'index15.html')


def indexend(request):
    msg = "Все хорошо"
    print(msg)
    Lg = request.session["Lg"]
    return render(request, 'indexend.html', {'Lg': Lg})


def export_xls(request):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Canvas.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('canvas list')  # this will make a sheet named Users Data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['id', 'Year',
               'sex', 'country1', 'country2', 'lang',
               'edu', 'shade', 'color1', 'color2', 'color3', 'color4', 'color5',
               'choice1', 'choice2', 'choice3', 'choice4', 'choice5', 'choice6', 'choice7', 'choice8', 'choice9',
               'choice10', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Client_Color1.objects.order_by('Client_id').values_list('Client_id', 'Client_Year',
                                                                   'Client_sex', 'Client_country1', 'Client_country2',
                                                                   'Client_lang',
                                                                   'Client_edu', 'Client_shade', 'color1', 'color2',
                                                                   'color3', 'color4',
                                                                   'color5',
                                                                   'left1', 'left2', 'left3', 'left4', 'left5', 'left6',
                                                                   'left7', 'left8',
                                                                   'left9', 'left10', )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response

# СУБЪЕКТЫ РФ


def russias_regions(request):
    msg = 'Когда вы заполните все поля анкеты, нажмите "продолжить" чтобы перейти к странице выбора цвета.'
    if request.method == "POST":
        form = Client_ColorForm_reg(request.POST)
        print("мы тут")
        if form.is_valid():
            print("в if провалились")
            print("а форму не сохранили")
            client = form.save()  # commit=False)
            print("и форму сохранили")
            print(client.Client_sex)
            print(client.Client_edu)
            print(client.Client_Year)
            msg = client.Client_id
            # Set a session value:
            request.session["User_id"] = client.Client_id
            # добавила Самойлова 24.5.22
            key = client.Client_id
            current_user = Client_Color2.objects.get(pk=key)
            date = datetime.datetime.today()
            current_user.color_like = date.strftime("%m/%d/%Y, %H:%M:%S")
            current_user.save(update_fields=['color_like'])
            # конец добавки
            Lg = "ru"
            next = "ПРОДОЛЖИТЬ"
            return render(request, 'fav_color.html', {'form': form, 'message': msg, 'Lg': Lg, 'next': next})
    else:
        form = Client_ColorForm_reg()
        request.session["Lg"] = "ru"
        Lg = "ru"
        next = "ПРОДОЛЖИТЬ"
        msg = 'Когда вы заполните все поля анкеты, нажмите "продолжить" чтобы перейти к странице выбора цвета.'
    return render(request, 'russias_regions.html', {'form': form, 'message': msg, 'Lg': Lg, 'next': next})


def fav_color(request):
    msg = "Все хорошо"
    if request.method == "POST":
        MyColor = request.POST['mycolor']
        key = request.session["User_id"]
        current_user = Client_Color2.objects.get(pk=key)
        # удалить все, кроме чистой даты   -  вставила  самойлова 28.05.22
        s = current_user.color_like.strip('/')  # вставила  самойлова 28.5.22
        if (s[0] == '#'):  # вставила  самойлова 28.5.22
            s = s[8:16]  # вставила  самойлова 28.5.22 оставляем только дату
        current_user.color_like = MyColor + '/' + s + '/'  # изменила самойлова 28.5.22
        current_user.save(update_fields=['color_like'])  # изменила самойлова 24.5.22
        print(current_user.color_like)
        # добавила Самойлова 24.5.22
        date = datetime.datetime.today()
        current_user.color_dislike = date.strftime('%H:%M:%S')
        current_user.save(update_fields=['color_dislike'])
        print(current_user.color_dislike)
        # конец добавки
        print(msg)
        Lg = "ru"
        next = "ПРОДОЛЖИТЬ"
        return render(request, 'fav_color.html', {'message': msg, 'Lg': Lg, 'next': next})
    else:
        msg = "Плохие данные"
        print(msg)
    return render(request, 'fav_color.html')


def export_regions_xls(request):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Canvas_regions.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('canvas list')  # this will make a sheet named Users Data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['id', 'Year',
               'sex', 'country1', 'country2', 'region', 'lang',
               'edu', 'shade', 'color_like', 'color_dislike', 'color1', 'color2', 'color3', 'color4', 'color5',
               'choice1', 'choice2', 'choice3', 'choice4', 'choice5', 'choice6', 'choice7', 'choice8', 'choice9',
               'choice10', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Client_Color2.objects.order_by('Client_id').values_list('Client_id', 'Client_Year',
                                                                   'Client_sex', 'Client_country1', 'Client_country2',
                                                                   'Client_region',
                                                                   'Client_lang',
                                                                   'Client_edu', 'Client_shade',
                                                                   'color_like', 'color_dislike',
                                                                   'color1', 'color2',
                                                                   'color3', 'color4',
                                                                   'color5',
                                                                   'left1', 'left2', 'left3', 'left4', 'left5', 'left6',
                                                                   'left7', 'left8',
                                                                   'left9', 'left10', )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/export_xls/
# http://127.0.0.1:8000/export_regions_xls/
# python manage.py runserver
