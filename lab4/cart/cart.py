from decimal import Decimal
from django.conf import settings
from pharmacy_app.models import Medicines


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, medicines, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        medicines_id = str(medicines.id)
        if medicines_id not in self.cart:
            self.cart[medicines_id] = {'quantity': 0,
                                    'price': str(medicines.price)}
        if update_quantity:
            self.cart[medicines_id]['quantity'] = quantity
        else:
            self.cart[medicines_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, car):
        """
        Удаление товара из корзины.
        """
        medicines_id = str(car.id)
        if medicines_id in self.cart:
            del self.cart[medicines_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        medicines_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        medicines = Medicines.objects.filter(id__in=medicines_ids)
        for medicine in medicines:
            self.cart[str(medicine.id)]['car'] = medicine

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                self.cart.values())
    
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True