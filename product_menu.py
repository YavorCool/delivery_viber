import answer_types
import colors


def make_buttons(products):
    buttons = []
    for product in products:
        preview_button_template = {
            "Columns": 2,
            "Rows": 2,
            "ActionType": "reply",
            "ActionBody": answer_types.PRODUCT_BTN + "_" + product['id'],
            "BgColor": colors.BEIGE,
            "Image": product['image_url']
        }

        descr_button_template = {
                "Columns": 4,
                "Rows": 2,
                "BgColor": colors.BEIGE,
                "ActionType": "reply",
                "ActionBody": answer_types.PRODUCT_BTN + "_" +  product['id'],
                "Text": "<b>{}</b><br><i>{}</i><br>Цена: <b>{}</b>".format(product['title'], product['subtitle'], product['price']),
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
              }
        buttons.append(preview_button_template)
        buttons.append(descr_button_template)

    buttons.append({
                "Columns": 6,
                "Rows": 1,
                "BgColor": colors.BEIGE,
                "ActionType": "reply",
                "ActionBody": answer_types.PRODUCT_BTN + "_" + answer_types.BACK_BTN,
                "Text": "<b>{}</b>".format('НАЗАД'),
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
              })

    return buttons


def get_product_menu(products):
    menu = {
        "Type": "keyboard",
        "BgColor": "#ffffff",
        "Buttons": make_buttons(products)
    }
    return menu
