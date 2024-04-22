class Queries:
    CREATE_REVIEW_TABLE = """
        CREATE TABLE IF NOT EXISTS review (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            contact TEXT, 
            date_visit INTEGER, 
            food_quality TEXT, 
            clean_est TEXT, 
            add_comment TEXT
        )
    """


    CREATE_MENU_TABLE = """
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """


    CREATE_FOOD_TABLE = """
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            picture TEXT,
            menu_id INTEGER, 
            FOREIGN KEY (menu_id) REFERENCES menu(id)
        )
    """

    DROP_MENU_TABLE = """DROP TABLE IF EXISTS menu"""
    DROP_FOOD_TABLE = """DROP TABLE IF EXISTS foods"""


    POPULATE_MENU_TABLE = """
        INSERT INTO menu (name)
        VALUES ('Закуски'), ('Салаты'),
        ('Супы'), ('Открытый огонь и Хоспер'), 
        ('Сезоны Кыргызстана'), ('Мясо, Рыба, Птица'), 
        ('Гарниры'), ('На Компанию'),
        ('Десерты'), ('Хлеб и Выпечка')
    """


    POPULATE_FOOD_TABLE = """
        INSERT INTO foods (name, price, picture, menu_id)
        VALUES ('Восточное овощное ассорти', 2200, 'images/assorti_snacks.jpeg', 1), 
        ('Греческий', 450, 'images/Grech_salat.jpg', 2), 
        ('Уха с семгой и форелью', 450, 'images/Uha_soup.jpg', 3), 
        ('Седло барашка', 650, 'images/Baranirebra_fire.jpg', 4), 
        ('Форель с овощами', 600, 'images/forel_kg.jpeg', 5), 
        ('Баранья голень с хумусом и табуле', 1250, 'images/BRSHK_meat.jpg', 6), 
        ('Рис отварной', 100, 'images/Rise_garnish.jpg', 7), 
        ('Ассорти по-восточному', 3900, 'images/BRSHK_comp.jpg', 8), 
        ('Мороженое', 300, 'images/IceCream_desert.jpeg', 9), 
        ('Токоч', 60, 'images/Lepeshka_bread.jpg', 10)
    """
