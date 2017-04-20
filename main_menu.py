import answer_types
import colors
MAIN_MENU = {
        "Type": "keyboard",
        "BgColor": "#FFFFFF",
        "Buttons": [
          {
            "Columns": 6,
            "Rows": 1,
            "BgColor": colors.BEIGE,
            "ActionType": "reply",
            "ActionBody": answer_types.MAIN_MENU_MENU_BTN,
            "Text": "Меню",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 60,
            "TextSize": "regular"
          },
          {
            "Columns": 6,
            "Rows": 1,
            "BgColor": colors.BEIGE,
            "ActionType": "reply",
            "ActionBody": answer_types.MAIN_MENU_SHOW_CART_BTN,
            "Text": "Корзина",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 60,
            "TextSize": "regular"
          },
          {
            "Columns": 6,
            "Rows": 1,
            "BgColor": colors.BEIGE,
            "ActionType": "reply",
            "ActionBody": answer_types.MAIN_MENU_CLEAR_CART_BTN,
            "Text": "Очистить корзину",
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 60,
            "TextSize": "regular"
          }
        ]
    }

CANCEL = {
        "Type": "keyboard",
        "BgColor": "#FFFFFF",
        "Buttons": [
          {
            "Columns": 6,
            "Rows": 1,
            "BgColor": colors.BEIGE,
            "ActionType": "reply",
            "ActionBody": answer_types.CANCEL_BTN,
            "Text": "<b>{}</b>".format('ОТМЕНА'),
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 60,
            "TextSize": "regular"
          },]
}