import redis
import json

#Корзина, ее сериализация и десериализация


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []
        self.db = redis.StrictRedis(host='127.0.0.1', port=6379)
        self.deserialize()

    def __str__(self):
        cart_str = ""
        total_pay = 0
        for item in self.items:
            cart_str += item['product']['title'] + " Кол-во: {}\n".format(item['count'])
            total_pay += int(item['product']['price']) * int(item['count'])
        cart_str += "Всего к оплате: {}".format(total_pay)
        return cart_str

    def serialize(self):
        return json.dumps(self.items)

    def deserialize(self):
        data = self.read_from_db()
        if data:
            self.items = json.loads(data.decode('utf-8'))

    def write_to_db(self):
        self.db.set(self.user_id, self.serialize())

    def read_from_db(self):
        return self.db.get(self.user_id)


if __name__ == "__main__":

    items = [
        {"id": "1", "name": "item_1"},
        {"id": "2", "name": "item_2"},
        {"id": "3", "name": "item_3"}
    ]


    cart = Cart("1")
    cart.items = items
    cart.write_to_db()

    cart = Cart("1")
    print(cart.items)

    cart = Cart("10")
    print(cart.items)




