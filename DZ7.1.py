class Product:
	def __init__(self, name, weight, category):
		self.name = name
		self.weight = weight
		self.category = category

	def __str__(self):
		return f'{self.name}, {self.weight}, {self.category}'


product = Product('Potato', 20, 'vegetablles')

class Shop:
	def __init__(self):
		self.__file_name = 'products.txt'

	def get_products(self):
		spisok = ''
		with open('products.txt', 'r', encoding='utf-8') as file:
			for i in file:
				spisok += i
		return spisok

	def add(self, *products):
		file = open('products.txt', 'r', encoding='utf-8')
		# content = file.read()
		sp = self.get_products()
		file.close()
		for product in products:
			product_str = f"{product.name},{product.weight},{product.category}"
			if product_str in sp:
				print(f'Продукт {product_str} уже есть в магазине')
			else:
				file = open('products.txt', 'a', encoding='utf-8')
				file.write(product_str + '\n')
				file.close()
#
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
