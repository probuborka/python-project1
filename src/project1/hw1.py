"""Модуль для работы с данными клиентов и заказов.

Содержит: 
- Класс CustomerDataClass данные клиента
- Класс OrderDataClass данные заказа 
- Функции расчета скидок и формирование отчета по клиенту
"""
class CustomerDataClass:
   """Класс - клиент."""
   def __init__(self,customer_id,customer_name):
      """Инициализирует объект клиента.
        
      Args:
         customer_id: Уникальный идентификатор клиента
         customer_name: Имя клиента
      """
      self.CustomerId=customer_id
      self.CustomerName=customer_name
      self.Orders=[]

   def add_order(self,order_object):
      """Добавляет заказ клиенту.
        
      Args:
         order_object: Объект заказа
      """
      self.Orders.append(order_object)

   def get_total_amount(self):
      """Рассчитывает общую сумму всех заказов клиента.
        
      Returns:
         Общая сумма заказов
      """
      total=0
      for o in self.Orders:
            total = total + o.amount
      return total

class OrderDataClass:
   """Класс - заказ."""

   def __init__(self,order_id,amount):
      """Инициализирует объект заказа.
        
      Args:
         order_id: Уникальный идентификатор заказа
         amount: Сумма заказа
      """
      self.orderId=order_id
      self.amount=amount

def calculate_discount(customer_obj):
   """Рассчитывает скидку.
   
   Args:
      customer_obj: Объект клиента
      
   Returns:
      Размер скидки
   """
   total_amount = customer_obj.get_total_amount()
   discount = total_amount * 0.1 if total_amount > 1000 else 0
   return discount

def print_customer_report(customer_obj):
   """Выводит отчет по клиенту.
   
   Args:
      customer_obj: Объект клиента
   """
   print('Customer Report for:',customer_obj.CustomerName)
   print('Total Orders:', len(customer_obj.Orders))
   print('Total Amount:', customer_obj.get_total_amount())
   print('Discount:',calculate_discount(customer_obj))
   if len(customer_obj.Orders) > 0:
      print('Average Order:',customer_obj.get_total_amount()/len(customer_obj.Orders))

def main_program():
   """Основная функция программы."""
   c1=CustomerDataClass(1,'SAP Customer')
   o1=OrderDataClass(101,500)
   o2=OrderDataClass(102,800)
   c1.add_order(o1)
   c1.add_order(o2)

   print_customer_report(c1)

   c2=CustomerDataClass(2,'Empty Customer')
   print_customer_report(c2) 

main_program()