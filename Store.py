class Store():
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.items = {}
  def add_item(self, item_name, price):
    self.items[item_name] = price
    print(f'товар {item_name} был добавлен в {self.name}')

  def remove_item(self, item_name):
    if item_name in self.items:
      del self.items[item_name]
      print(f'товар {item_name} был удален из {self.name}')
    else:
      print(f'товар {item_name} не найден в {self.name}')

  def get_price(self, item_name):
    return self.items.get(item_name)

  def update_price(self, item_name, new_price):
    if item_name in self.items:
      self.items[item_name] = new_price
      print(f'цена товара {item_name} была изменена на {new_price}')
    else:
      print(f'товар {item_name} не найден в {self.name}')



store1 = Store("Магазин 1", "ул. Ленина, 1")
store2 = Store("Супермаркет", "пр. Победы, 10")
store3 = Store("Лавка", "ул. Мира, 5")

store1.add_item("Яблоки", 100.0)
store1.add_item("Хлеб", 50.0)
store1.add_item("Гречка", 90.0)

store1.remove_item("Хлеб")

store1.update_price(item_name="Яблоки", new_price=150.0)

