# Модуль 9. Задание 7. Метод бутерброда
#
# Напишите программу-дешифратор, которая расшифровала бы введённые «методом бутерброда» сообщения.
#
# Пример:
# Введите зашифрованное сообщение: shacnidw.
# Расшифрованное сообщение: sandwich.
#
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
# переменные имеют значащие имена, не только a, b, c, d (видео 2.3).
# в сложении строк можно менять слагаемыми местами, но такая перемена изменит результат:
# строка += “а” – так вы добавите символ в конец строки
# строка = “а” + строка – так вы добавите символ в начало строки (что позволит сложить строку задом наперед)

input_word = 'К.аакп ивти-дeнlоb,a tвu mлmиiт ехрыанлньандо йз иф оорнмьел ектоирчтюелжк сpиy tьhтoяnо т3с озса пыинсжылвоаде т)сsяt cвi dв(и дйее рпаовсоллесд оивчаютлекл ьрнеомситрип аэНл е.мйеиннтеочва нвз  кхрыумгеляынхе мсзкиоебнк атхе,у бве ртто  nвoрhеtмyяp  кхаыкр одтлояк  стпои с,кхоывн нхаадр ахкатреуртнкыу рктвса дхрыантьнлыеед.т оН евк оытмоирныеем иорспо биежненторсотки  —к охрытненжаедй :х аорнуит куупротрся дхоичгеунрыд  пво  eпlоpзuиtц иеяимн;а вtоuзpьlлeо пмсоИг у.тм ыхнрсаанпиотзье би  ис омдыемрежааттиьч  венеулторби  дсоекб яь тоаблъеедкст ыт юляюлбоывхз отпи п,оивм а(жие тдраожке  есыонснтаадванзы х,)ы;т ндаотсстнуопК  к. тэнлаетмсеннотка мь лпорро иаснх оидмиатт апдои дснмаекщ еинмиыюн,ь лаа ендеи  пьот ыкбл юмчиу ;т евя лроавмзкоапх  еэжткоайт  сьттрсуокмтеуярные мдзаиненны х—  оьптрсеоднеслаепноыз евБс е. аокпсеирпасц ииим,а тонсенноовпамнонкы ес  нмае чп р,иемеернтесныиби  осммоедщеевнаизя  я(ситнюдяенклсоипрыовв аинмиает,н есмреелзэ) ;х ик оср тиеижциа рпеопдод еурмжоитвэаоюпт  ,нмеоозгаррабнои чмеынбноосео  киотляимчаепс твв оя сутряонванрехй  ивжлеотжреонкн оисттсио;м екяонретмезжиие нх реанниячти рупк аозПа т.етлюиа тноаб адрр уегеирет соыббъ еикжтеыт,р оак  з—н аьчтисто риохк См о.жвноок спирпесд сттоа вхлия тььт,а чкиалкт ом аоснсдиовгыы вс стыелжоокм;  ,ойноир оппо з,вйоелжяеюттр оокч еонвьт спйроовсст оо тмэе ноянтнье ммие с—т аьмтис озмнеаячнеенмизяи едНв у:хт епветрое моегненны ха.н  Зяасчтеёмд йиаснп оалкьыззояв айтеьл ектоардтзеожс  вум е,сятсот есепмиусзкаар?  ,Тоенм ,, скотроп оувж ей ыунснпеевлт спеотзснеа кеонмлиотпьвс яо тсЭо  .сепшиьслкоабм ие жва дP yиt hеoоnм,а см оежже то тп оёксавз аьттьасляе дн ет уогчоемв иидкнсыимп сс м,ыисклс еичсиптоклаьфз оьвдаенВи я. йкеожрет'

correct = 0
if len(input_word) % 2 == 0:
    correct = 1

len_word = len(input_word)
result = input_word[0:len_word:2] + input_word[(len_word - 2 + correct):0:-2]

print(f"Зашифрованное слово: {result}")