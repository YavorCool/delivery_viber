import answer_types, colors, product_categories

CATEGORIES_MENU = {
        "DefaultHeight": "true",
        "Type": "keyboard",
        "BgColor": "#FFFFFF",
        "Buttons": [
          {
            "Columns": 6,
            "Rows": 1,
            "BgColor": colors.BEIGE,
            "ActionType": "reply",
            "ActionBody": answer_types.CATEGORY_BTN + "_" + product_categories.BURGER,
            "Text": "Бургеры",
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
            "ActionBody": answer_types.CATEGORY_BTN + "_" + product_categories.PIZZA,
            "Text": "Пицца",
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
            "ActionBody": answer_types.CATEGORY_BTN + "_" + product_categories.SUSHI,
            "Text": "Суши",
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
            "ActionBody": answer_types.CATEGORY_BTN + "_" + product_categories.OTHER,
            "Text": "Разное",
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
            "ActionBody": answer_types.CATEGORY_BTN + "_" + answer_types.BACK_BTN,
            "Text": "<b>{}</b>".format('НАЗАД'),
            "TextVAlign": "middle",
            "TextHAlign": "center",
            "TextOpacity": 60,
            "TextSize": "regular"
           }
        ]
    }
