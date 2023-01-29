class knap:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight

def frac_knap(capacity, arr):

	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
	finalprofit = 0.0
	for knap in arr:
		if knap.weight <= capacity:
			capacity -= knap.weight
			finalprofit += knap.profit
		else:
			finalprofit += knap.profit * capacity / knap.weight
			break
	return finalprofit

capacity = 100
arr = [knap(50,60), knap(200,10), knap(80,20)]

max_val = frac_knap(capacity, arr)
print ('max profit = {}'.format(max_val))
