f=open('text.txt','r',encoding="utf-8",)#открываем файл
print(" Слова : ",len(f.split()))#разбиваем строку из файла на слова
f.close()#закрываем файл
