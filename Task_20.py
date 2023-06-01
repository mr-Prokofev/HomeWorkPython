# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

def Word_Verification(stroka): # Проверка однородсности букв
    count_i = 0
    if stroka.isalpha():
        for i in stroka.upper():
            if 65 <= ord(i) <= 90:
                count_i+=1
            else:
                count_i-=1
    if count_i == len(stroka):
        return 0
    elif  count_i == -len(stroka):
        return 1
    else:
        return 2 

def DictCount(stroka, num):
    count=0
    for i in input_stroka.upper():
        for key in my_list_dictionary_en_ru[num]:
            if i in key:
                count+=my_list_dictionary_en_ru[num].get(key)
    return count

my_list_dictionary_en_ru = [{               # список словарей 0 - en, 1 - ru
    'AEIOULNSTR' : 1, 
    'DG' : 2, 
    'BCMP' : 3,
    'FHVWY' : 4, 
    'K' : 5, 
    'JX' : 8, 
    'QZ' :10
                }, 
    {
    "АВЕИНОРСТ": 1,
    "ДКЛМПУ": 2,
    "БГЁЬЯ" : 3,
    "ЙЫ": 4,
    "ЖЗХЦЧ": 5,
    "ШЭЮ":8,
    "ФЩЪ": 10
    }]

input_stroka = input("Введите слово: ")
dict_num = Word_Verification(input_stroka)

if 0<= dict_num <= 1:
    dictCount = DictCount(input_stroka, dict_num)
    print(dictCount)
else:
    print("Неверные данные. Попробуйте изменить.")