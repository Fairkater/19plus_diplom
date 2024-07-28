import sender_stand_request
import data


def test_create_and_get_order():
    #Создание заказа
    response = sender_stand_request.post_new_order(data.order_body)

    #Сохранение номера трека заказа
    track_number = response.json().get("track")

    #Получение заказа по треку
    response = sender_stand_request.get_order_by_track(track_number)

    #Проверка кода ответа
    assert response.status_code == 200

    # Виталий Новиков, 19-я когорта — Финальный проект. Инженер по тестированию плюс