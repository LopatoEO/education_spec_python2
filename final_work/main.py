from enum import Enum
from sqlalchemy import create_engine
from db_handler.crud import BaseCrud
from prettytable import PrettyTable
from exceptions.exceptions import UniqueCardError

class PaySystem(Enum):
    RUSSIANPAYMENTSYSTEM = [['2'], 'Мир', True]
    DINERCLUB =  [['30', '36', '38'],  'Diners Club', False]
    JCBINTERNATIONAL = [['31', '35'], 'JCB International', False]
    AMERICANEXPRESS = [['34', '37'], 'American Express', False]
    VISA = [['4'],'VISA', True]
    MAESTRO = [['50', '56', '57', '58', '63', '67'], 'Maestro', False]
    MASTERCARD = [['51', '52', '53', '54', '55'], 'MasterCard', True]
    DISCOVER =  [['60'], 'Discover', False]
    CHINAUNIOPAY = [['62'], 'China UnionPay', True]
    UNIVERSALCARDSYSTEM = [['7'], 'УЭК (Универсальная электронная карта)', True]

    @classmethod
    def get_system(cls, code):
        for item in cls:
            for number in item.value[0]:
                if code[0:len(number)] == number:
                    return item.value[1], item.value[2]
        return "Неустановленная платёжная система", False 
                
class Validator:
    @staticmethod
    def validate_card(card_code):
        card_code = card_code.replace(" ","")
        digitList = []
        for index in range(len(card_code)):
            char = int(card_code[index])
            if (index % 2) == 0:
                char *= 2
            if char > 9:
                char = int(str(char)[0]) + int(str(char)[1])
            digitList.append(char) 
        return (sum(digitList) % 10) == 0
    
class CardBank:
    def __init__(self, db):
        self.db = db
        self.cardList = []
        print(self.db.get_cards())
        for item in self.db.get_cards():
            self.cardList.append(Card( 
                                      item['user'],
                                      item['cardCode']
            ))

    def add_card(self, user, cardCode):
        try:
            card = Card(user, cardCode)
            self.cardList.append(card)
            self.db.insert_card(card)
        except (TypeError, UniqueCardError) as e:
            print(e)
    
    def delete_card(self, user, cardCode):
        card = list(filter(lambda x: x.user == user and x.cardCode == cardCode, self.cardList))[0]
        self.db.delete_card_by_name(card)
        self.cardList.remove(card)
    
    def get_cards_from_file(self, path):
        file = open(path, 'r', encoding='utf-8')
        cards = list(map(lambda x: x.replace('\t', '').replace('\n', '').split(", "),
                            file.readlines()))
        for item in cards:
            try:
                card = Card(item[0], item[1])
                self.db.insert_card(card)
                self.cardList.append(card)
            except (TypeError, UniqueCardError) as e:
                print(e)

    def __str__(self) -> str:
        mytable = PrettyTable()
        mytable.field_names = ["Пользователь",
                                "Номер карты",
                                "Ошибки в номере", 
                                "Система",
                                "Оплата"]
        for item in self.cardList:
            mytable.add_row([item.user,
                            item.cardCode,
                            item.isValid,
                            item.system,
                            item.paymentAllowed])
        return str(mytable)


class Card:
    def __init__(self, user, cardCode):
        if not(isinstance(user, str) and isinstance(cardCode, str)):
            raise TypeError("Введены некорректные данные")
        self.user = user
        self.cardCode = cardCode
        self.isValid = Validator.validate_card(cardCode)
        self.system, self.paymentAllowed = PaySystem.get_system(cardCode)
        



if  __name__ == '__main__':
    db = BaseCrud("sqlite:///db/card_base.db")
    cb = CardBank(db)
    cb.add_card("Иван Иванов", "4274 9910 0017 1851")
    print(cb)
    cb.delete_card("Иван Иванов", "4274 9910 0017 1851")
    print(cb)
    cb.get_cards_from_file('card_list.txt')
    print(cb)


    
    