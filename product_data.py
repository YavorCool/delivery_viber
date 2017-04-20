import product_categories

products = [{'id': '1',
             'title': 'Гамбургер',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17904049_749420091898582_7046445455780381383_n.png?oh=44013266a0e4fdb9340b9955366dd98e&oe=598CEBDF',
             'subtitle': 'Бургер с одной котлетой',
             'price': "100",
             'category': product_categories.BURGER
             },
            {'id': '2',
             'title': 'Двойной Гамбургер',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17362479_749420041898587_4204192282191711541_n.jpg?oh=ccdbdb13d59fed49e5e5699a555b54a3&oe=59857ABC',
             'subtitle': 'Бургер с двумя котлетами',
             'price': "150",
             'category': product_categories.BURGER
             }
            ,
            {'id': '3',
             'title': 'Пицца салями',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t31.0-8/17973452_749420105231914_3673184004882386026_o.jpg?oh=597075e5a23da5ac747d9185301cc307&oe=59866752',
             'subtitle': 'Сыр, колбаса, соус, помидоры',
             'price': "170",
             'category': product_categories.PIZZA
             }
            ,
            {'id': '4',
             'title': 'Пицца с ветчиной',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17862763_749420038565254_8947966646929473572_n.jpg?oh=1b840c9ede076319d73da3e849422456&oe=5994BBED',
             'subtitle': 'Тонкое тесто, сыр, ветчина, грибы',
             'price': "350",
             'category': product_categories.PIZZA
             }
            ,
            {'id': '5',
             'title': 'Филадельфия',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17757639_749420045231920_1068338302177148852_n.jpg?oh=a7b79ca37cba5a5f4bb823797b9fa27a&oe=5956BF8C',
             'subtitle': 'Рыба, рис итд итп',
             'price': "250",
             'category': product_categories.SUSHI
             },
            {'id': '6',
             'title': 'Маки каки',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17991990_749784785195446_1410928244934943134_n.jpg?oh=a33bf9f2eab296ef87e76bc01a4014b7&oe=598904C6',
             'subtitle': 'Рыба, рис итд итп',
             'price': "255",
             'category': product_categories.SUSHI
             },
            {'id': '7',
             'title': 'Маки макаки',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17990836_749784835195441_2273263083197903197_n.jpg?oh=299fe2193285e6036c3f6809d0cce415&oe=59889B3F',
             'subtitle': 'Рыба, рис итд итп',
             'price': "255",
             'category': product_categories.SUSHI
             },
            {'id': '8',
             'title': 'Баклажаны',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17991814_749784988528759_8986870479560840033_n.jpg?oh=d4309d7de567602e09188d3d3bbb984a&oe=598CDA8C',
             'subtitle': 'Вкусно с соусом все дела',
             'price': "150",
             'category': product_categories.OTHER
             },
            {'id': '9',
             'title': 'Салат с курицей',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17952780_749784788528779_1816893309270379746_n.jpg?oh=169b9dcb06375d12248da70b7d4a0746&oe=5982A906',
             'subtitle': 'Салат с курицей',
             'price': "750",
             'category': product_categories.OTHER
             },
            {'id': '10',
             'title': 'Макаки масасаки',
             'image_url': 'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/17904102_749784781862113_1480254221746574575_n.jpg?oh=fbcb4569c3e6935dfb4793d403a675d0&oe=59928F10',
             'subtitle': 'Рыба, рис итд итп',
             'price': "450",
             'category': product_categories.SUSHI
             }
            ]


def get_product_by_id(id):
    for product in products:
        if id == product['id']:
            return product


def get_products_by_category(category):
    data = []
    for product in products:
        if product['category'] == category:
            data.append(product)
    return data


if __name__ == "__main__":
    print(get_product_by_id("4"))
    print(get_products_by_category(product_categories.PIZZA))