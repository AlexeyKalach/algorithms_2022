"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""
# Изначальный код:
def num_translate(adv_en_num=None):
    """Переводит числительные от 0 до 10 с английского нужном регистре"""

    translate_dict = {'zero': 'ноль',
                      'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять'}

    print(f'Размер словаря: {getsizeof(translate_dict)}')
    if 64 < ord(adv_en_num[0]) < 91 and adv_en_num.lower() in translate_dict:
        return f'{str(translate_dict[adv_en_num.lower()]).capitalize()}'
    elif adv_en_num in translate_dict:
        return f'{translate_dict[adv_en_num]}'
    else:
        return None

# Оптимизация: использовал именованный кортеж, скоратил объемы использованной памяти
def optimized(adv_en_num=None):
    """Переводит числительные от 0 до 10 с английского нужном регистре"""

    nt = namedtuple('translate_dict',
                                ('zero', 'one', 'two', 'three', 'four', 'five',
                                 'six', 'seven', 'eight', 'nine', 'ten'))

    a = nt(zero='ноль', one='один', two='два', three='три',
           four='четыре', five='пять', six='шесть', seven='семь',
           eight='восемь', nine='девять', ten='десять')

    print(f'Размер именовоанного кортежа: {getsizeof(a)}')
    if 64 < ord(adv_en_num[0]) < 91 and adv_en_num.lower() in a._asdict():
        return f'{str(a._asdict()[adv_en_num.lower()]).capitalize()}'
    elif adv_en_num in a:
        return f'{a._asdict()[adv_en_num]}'
    else:
        return None


if __name__ == '__main__':

    num_translate('one')
    optimized('one')

