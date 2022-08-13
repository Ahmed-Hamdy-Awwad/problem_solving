import csv, os


def calculate():
	file_name = input('Enter file name: ')
	file_name_text , file_name_extension = os.path.splitext(file_name)
	if not file_name_extension:
		print('Please make sure file has .csv extension')
		return

	try:
		orders_count = 0
		for r in open(file_name):
			orders_count += 1
	except:
		print('File does not exist')
		return

	# Constraints
	# 1 ≤ number of rows of data ≤ 10^4
	if orders_count < 1:
		print('There is no data in the file')
		return
	if orders_count > 10000:
		print('Data is very big to be processed')
		return

	initial_data = {}
	file_1 = []
	file_2 = []

	with open(file_name) as data_file:
		orders = csv.reader(data_file, delimiter=',')

		for order in orders:
			try:
				product = initial_data[order[2]]
				product['total_qty'] += float(order[3])
				product['avg_qty'] = round((product['total_qty'] / orders_count), 3)
				try:
					brands = product['brands']
					brands[order[4]] += 1
				except:
					brands[order[4]] = 1
			except:
				initial_data[order[2]] = {"total_qty": float(order[3]), 'avg_qty': round((float(order[3]) / orders_count), 3), 'brands': {order[4]: 1}}
		
		for product in initial_data:
			file_1.append([product, initial_data[product]['avg_qty']])
			brands = initial_data[product]['brands']
			max_count = 0
			brand_name = ''
			for brand in brands:
				if brands[brand] > max_count:
					max_count = brands[brand]
					brand_name = brand
			file_2.append([product, brand_name])
	try:
		with open('0_'+file_name, 'w', newline='') as f1:
			writer = csv.writer(f1)
			writer.writerows(file_1)
	except:
		print('Could not create the results file')
		return
	try:
		with open('1_'+file_name, 'w', newline='') as f2:
			writer = csv.writer(f2)
			writer.writerows(file_2)
	except:
		print('Could not create the results file')
		return

calculate()