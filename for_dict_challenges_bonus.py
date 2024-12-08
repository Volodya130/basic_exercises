"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
import pprint

def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def Message_counter(messages):      #создаем словарь авторов с количеством написанных сообщений
    writers = {}
    for message in messages:
        id_writer = message['sent_by']
        if id_writer in writers:
            writers[id_writer] += 1
        else:
            writers[id_writer] = 1
    return writers

def Ultra_Message(messages):        #сщздаем словарь из сообщений с количеством ответов на них
    umessage = {}
    for message in messages:
        id_message = message['reply_for']
        if id_message is None:
            pass    
        elif id_message in umessage:
            umessage[id_message] += 1
        else:
            umessage[id_message] = 1
    return umessage

def most_viewed_authors(messages):        #создаем словарь из авторов и просмартивающих пользователей
    stat = {}
    stata = []
    for message in messages:
        id_writer = message['sent_by']
        audience = message['seen_by']
        if id_writer not in stata:
            stat[id_writer] = audience
            stata.append(id_writer) 
        else:
            stat[id_writer].extend(audience)
    for autor in stat:
        stat[autor]=len(list(set(stat[autor]))) #количество уникальных просмотров по автору

    max_seen=0
    for autor in stat:
        if stat[autor] > max_seen:
            max_seen = stat[autor]
    
    list_max_autors = []
    for autor in stat:
        if stat[autor] == max_seen:
            list_max_autors.append(autor)
    return max_seen, list_max_autors
        

def author_finder(mes_id, mess):        #ищем автора сообщения, на которое чаще отвечают
    author = ""
    for message in mess:
        if message['id'] == mes_id:
            author = message['sent_by']
    return author
    
def time_distribution(messages):        #ищем период времени когда чаще пишут  
    time_period = {"Утро":0, "День":0, "Вечер":0}
    for message in messages:
        t_message = int(message['sent_at'].strftime('%H')) #получаем час отправки сообщения
        if t_message < 12:
            time_period["Утро"] += 1
        elif t_message < 18:
            time_period["День"] += 1
        else:
            time_period['Вечер'] += 1
    return time_period

def greatest(writters):     #находим в словаре ключ, который имеет больший вес
    greatest_wr = ''
    count_message = 0
    for writter in writters:
        if writters[writter] > count_message:
            count_message = writters[writter]
            greatest_wr = writter
    return greatest_wr


def main():
    messages = generate_chat_history()
    
        
    wr = Message_counter(messages)
    mes = Ultra_Message(messages)
    sup_mes = greatest(mes)
    u = most_viewed_authors(messages)
    aftor = u[1]
    t = time_distribution(messages)
    t2 = greatest(t)
    

    print('1. Вывести айди пользователя, который написал больше всех сообщений.')
    print(f'Больше всех сообщений написал пользователь с ID: {greatest(wr)}')
    print('')
    print('2. Вывести айди пользователя, на сообщения которого больше всего отвечали.')
    print(f'Айди пользователя, на сообщения которого больше всего отвечали: {author_finder(sup_mes, messages)}')
    print('')
    print('3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.')
    print(f'Наибольшее количество раз ({u[0]}) пользователи смотрели этих авторов: {', '.join(map(str, aftor))}')
    print('')
    print('4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).')
    print(f'Период, когда пользователи пишут больше всего сообщений это: {t2}')
    print('')
    print('5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).')

if __name__ == "__main__":
    main()



