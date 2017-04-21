from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

import time
import logging
import sched
import threading
import json

from main_menu import MAIN_MENU, CANCEL
from categories_menu import CATEGORIES_MENU
from product_menu import get_product_menu
from product_data import get_products_by_category, get_product_by_id
import answer_types

from cart import Cart

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='',
    auth_token='45decab4eff228d7-e86f8a81930047f7-8e75c34b9894d46e'
))


@app.route('/', methods=['POST'])
def incoming():
    request_data = request.get_data().decode()
    logger.debug("received request. post data: {0}".format(request_data))

    viber_request = viber.parse_request(request_data)
    request_json = json.loads(request_data)

    msg = TextMessage(text='Выберите пункт меню', keyboard=MAIN_MENU)

    if isinstance(viber_request, ViberMessageRequest):
        msg_text = request_json['message']['text']
        if request_json['message'].get('tracking_data'):
            logger.debug('Message has tracking data: {}'.format(request_json['message']['tracking_data'].split('_')[0]))
            if request_json['message']['tracking_data'].split('_')[0] == answer_types.CHOSEN_PRODUCT_ID_TRACKING_DATA:
                logger.debug('answer type ------- {}'.format(answer_types.CHOSEN_PRODUCT_ID_TRACKING_DATA))
                chosen_product_id = request_json['message']['tracking_data'].split('_')[1]
                if msg_text.isdigit():
                    if 10 >= int(msg_text) >= 1:
                        add_to_cart(Cart(viber_request.sender.id),
                                    get_product_by_id(chosen_product_id),
                                    int(msg_text))
                        msg = TextMessage(text='{}, в количестве {} добавлено в корзину'.format(
                            get_product_by_id(chosen_product_id)['title'],
                            msg_text),
                                          keyboard=MAIN_MENU)
                    else:
                        msg = TextMessage(text='Число должно быть от 1 до 10, введите еще раз',
                                          tracking_data=answer_types.CHOSEN_PRODUCT_ID_TRACKING_DATA + "_" + chosen_product_id,
                                          keyboard=CANCEL)
                else:
                    msg = TextMessage(text='Необходимо ввести число от 1 до 10',
                                      tracking_data=answer_types.CHOSEN_PRODUCT_ID_TRACKING_DATA + "_" + chosen_product_id,
                                      keyboard=CANCEL)
        if msg_text == answer_types.MAIN_MENU_MENU_BTN:
            logger.debug('answer type ------- {}'.format(answer_types.MAIN_MENU_MENU_BTN))
            msg = TextMessage(text='Выберите категорию', keyboard=CATEGORIES_MENU)

        elif msg_text == answer_types.CANCEL_BTN:
            logger.debug('answer type ------- {}'.format(answer_types.CANCEL_BTN))
            msg = TextMessage(text='Отмена', keyboard=MAIN_MENU)

        elif msg_text == answer_types.MAIN_MENU_SHOW_CART_BTN:
            logger.debug('answer type ------- {}'.format(answer_types.MAIN_MENU_SHOW_CART_BTN))
            cart = Cart(viber_request.sender.id)
            logger.debug('Cart is: ------------------------ {}'.format(cart))
            if cart.items.__len__() == 0 or cart is None:
                msg = TextMessage(text='Ваша корзина пуста', keyboard=MAIN_MENU)
            else:
                print(cart.__str__())
                msg = TextMessage(text=cart.__str__(), keyboard=MAIN_MENU)

        elif msg_text == answer_types.MAIN_MENU_CLEAR_CART_BTN:
            logger.debug('answer type ------- {}'.format(answer_types.MAIN_MENU_CLEAR_CART_BTN))
            clear_cart(Cart(viber_request.sender.id))
            msg = TextMessage(text='Корзина очищена', keyboard=MAIN_MENU)

        elif msg_text.startswith(answer_types.CATEGORY_BTN):
            logger.debug('answer type ------- {}'.format(answer_types.CATEGORY_BTN))
            if msg_text.split('_')[1] == answer_types.BACK_BTN:
                msg = TextMessage(text='Выберите пункт меню', keyboard=MAIN_MENU)
            else:
                msg = TextMessage(text='Выберите товар',
                                  keyboard=get_product_menu(get_products_by_category(msg_text.split('_')[1])))
        elif msg_text.startswith(answer_types.PRODUCT_BTN):
            logger.debug('answer type ------- {}'.format(answer_types.PRODUCT_BTN))
            if msg_text.split('_')[1] == answer_types.BACK_BTN:
                msg = TextMessage(text='Выберите категорию', keyboard=CATEGORIES_MENU)
            else:
                msg = TextMessage(text="Вы выбрали " + get_product_by_id(msg_text.split('_')[1])[
                    'title'] + "\n Введите количество товара от 1 до 10",
                                  tracking_data=answer_types.CHOSEN_PRODUCT_ID_TRACKING_DATA + "_" + msg_text.split('_')[1],
                                  keyboard=CANCEL)

        viber.send_messages(viber_request.sender.id, [
            msg
        ])

    elif isinstance(viber_request, ViberConversationStartedRequest):
        msg = TextMessage(text='Выберите пункт меню', keyboard=MAIN_MENU)
        viber.send_messages(viber_request.user.id, [
            msg
        ])

    elif isinstance(viber_request, ViberSubscribedRequest) \
            or isinstance(viber_request, ViberUnsubscribedRequest):
        pass
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)


def set_webhook(viber):
    viber.set_webhook('https://llkfncvzsx.localtunnel.me')


def add_to_cart(cart, product, count):
    for item in cart.items:
        if item['product']['id'] == product['id']:
            item['count'] += count
            cart.write_to_db()
            return item
    item = {"product": product, "count": int(count)}
    cart.items.append(item)
    cart.write_to_db()
    return item


def clear_cart(cart):
    cart.items = []
    cart.write_to_db()


if __name__ == "__main__":
    viber.set_webhook("")
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(5, 1, set_webhook, (viber,))
    t = threading.Thread(target=scheduler.run)
    t.start()

    app.run(host='0.0.0.0', port=8000, debug=True)
