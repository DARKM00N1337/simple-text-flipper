# функция переворота текста
def mixer(a):
    word = a[::-1]
    print(word)
# основной цикл
while True:
    ar = input('text?')
    mixer(ar)
    al = input('enter 1 for continue')
    if al != '1':
        break