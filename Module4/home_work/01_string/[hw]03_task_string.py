# Посчитайте количество согласных букв в данной строке.
text = 'езусловно высококачественный прототип будущего проекта позволяет выполнить важные задания по разработке ' \
       'распределения внутренних резервов и ресурсов А также диаграммы связей которые представляют собой яркий ' \
       'пример континентально-европейского типа политической культуры будут рассмотрены исключительно в разрезе' \
       ' маркетинговых и финансовых предпосылок'

consonants="бвгджзйклмнпрстфхцчшщ"
text=text.lower()
i = 0
total_consonants = 0
while i < len(consonants):
    total_consonants += text.count(consonants[i])
    i += 1

print(total_consonants)
