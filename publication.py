# class Publication:
#     def __init__(self, title, author, year):
#         self.title = title
#         self._author = author
#         self._year = year

#     def get_info(self):
#         return f'"{self.title}" ({self._author}, {self._year})'

class Publication:
    def __init__(self, title, author, year):
      self.is_available = True
      self.title = title
      self._author = author
      self._year = year


    def borrow(self):
        if self.is_available:
              self.is_available = False
              return f'Вы взяли книгу:"{self.title}"'
        else:
              return "Недоступно"



    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year})'
    
# obj = Publication("wow","pushkin", 1799)    

# while True:
#     choice = int(input("1) отдолжить книгу "))
#     if choice == 1:
#         print(obj.borrow())
#         print(obj.get_info())

   
