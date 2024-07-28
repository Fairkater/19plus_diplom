import configuration
# sender_stand_request.py
import requests
import configuration

def post_new_order(order_body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)
    return response

def get_order_by_track(track_number):
    response = requests.get(f"{configuration.URL_SERVICE + configuration.GET_ORDER_PATH}?t={track_number}")
    return response


