from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self,name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                self.__items[name] += count
                print("Нужное количество есть на складе")
                print(f"Курьер забрал {count} {name} со склад")
                print(f"Курьер везет {count} {name}  со склад в магазин")
                print(f"Курьер доставил {count} {name}  в магазин")
                return True
            else:
                print("Не хватает на складе, попробуйте заказать меньше")
                return False
        else:
            if self.get_free_space() >= count:
                self.__items[name] = count
                return True
            else:
                print("Недостатчно места на складе")
                return False

    def remove(self, name, count):
        if self.__items[name] >= count:
            print("Нужное количество есть на складе")

            self.__items[name] -= count
            return True
        else:
            print("Недостатчно места на складе")
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f" {value} {key}\n"
        return st


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print(" Много уникальных товаров")
            return False
        else:
            super().add(name, count)


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == "Доставить":
            self.__from = req_list[4]
            self.__to = req_list[6]
        elif action == "Забрать":
            self.__from = req_list[4]
            self.__to = None
        elif action == "Привезти":
            self.__from = req_list[6]
            self.__to = None

    def move(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.__item, self.__count):
                eval(self.__to).remove(self.__item, self.__count)
        elif self.__to:
            eval(self.__to).add(self.__item, self.__count)
        elif self.__from:
            eval(self.__to).remove(self.__item, self.__count)


склад = Store(items={"печеньки": 3, "собачки": 4, "коробки": 5})

магазин = Shop(items={"печеньки": 0, "собачки": 0, "коробки": 0})



