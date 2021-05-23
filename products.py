products = []
while True:
	name = input('請輸入消費商品 (離開輸入 q): ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	p = [name, price]
	products.append(p)
print(products)

with open('products.txt', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')

