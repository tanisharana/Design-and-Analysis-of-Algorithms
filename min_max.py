def max(arr, ind, len):
	maximum = -1;

	if (ind >= len - 2):
		if (arr[ind] > arr[ind + 1]):
			return arr[ind];
		else:
			return arr[ind + 1];


	maximum = max(arr, ind + 1, len);

	if (arr[ind] > maximum):
		return arr[ind];
	else:
		return maximum;


def min(arr, ind, len):
	minimum = 0;
	if (ind >= len - 2):
		if (arr[ind] < arr[ind + 1]):
			return arr[ind];
		else:
			return arr[ind + 1];

	minimum = min(arr, ind + 1, len);

	if (arr[ind] < minimum):
		return arr[ind];
	else:
		return minimum;


minimum, maximum = 0, -1;
print("enter array length")
n = int(input())
array=[]
print("enter array")
for i in range(0,n):
    ele=int(input())
    array.append(ele)
maximum = max(array, 0, n);
minimum = min(array, 0, n);
print("minimum = ", minimum,"\n");
print("maximum = ", maximum,"\n");