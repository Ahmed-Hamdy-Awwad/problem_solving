import unittest, program


class TestCalculate(unittest.TestCase):

	def test_calculate(self):
		expected_product_1 = 'Intelligent Copper Knife'
		expected_avg_1 = 2.4
		expected_brand_1 = 'Hilll-Gorczany'
		expected_product_2 = 'Small Granite Shoes'
		expected_avg_2 = 0.8
		expected_brand_2 = 'Rowe and Legros'

		actual_data = program.calculate()

		file_0 = actual_data['file_0']
		product_1_0 = file_0[0]
		product_2_0 = file_0[1]

		file_1 = actual_data['file_1']
		product_1_1 = file_1[0]
		product_2_1 = file_1[1]

		# Average quantity per order tests
		self.assertEqual(expected_product_1, product_1_0[0])
		self.assertEqual(expected_avg_1, product_1_0[1])

		self.assertEqual(expected_product_2, product_2_0[0])
		self.assertEqual(expected_avg_2, product_2_0[1])

		# Top brand tests
		self.assertEqual(expected_product_1, product_1_1[0])
		self.assertEqual(expected_brand_1, product_1_1[1])

		self.assertEqual(expected_product_2, product_2_1[0])
		self.assertEqual(expected_brand_2, product_2_1[1])

if __name__ == '__main__':
	test = TestCalculate()
	test.test_calculate()