from app import db, Pizza

# Створення об'єктів піц
pizza1 = Pizza(name="Маргарита", ingredients="Томати, моцарела, базилік", price=120)
pizza2 = Pizza(name="Пепероні", ingredients="Пепероні, томатний соус, сир", price=150)
pizza3 = Pizza(name="Чотири сири", ingredients="Моцарела, горгонзола, пармезан, чеддер", price=180)
pizza4 = Pizza(name="Гавайська", ingredients="Шинка, ананаси, моцарела, томатний соус", price=170)
pizza5 = Pizza(name="Капрічоза", ingredients="Гриби, шинка, артишоки, оливки, томатний соус, сир", price=200)

# Додавання в базу даних
db.session.add(pizza1)
db.session.add(pizza2)
db.session.add(pizza3)
db.session.add(pizza4)
db.session.add(pizza5)
db.session.commit()