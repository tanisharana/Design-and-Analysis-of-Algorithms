
import timeit 
def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array=[]
print("enter array length")
n = int(input())
print("enter array")
for i in range(0,n):
    ele=int(input())
    array.append(ele)
print("enter element to be found")
x=int(input())
result = linearSearch(array, n, x)
if(result == -1):
    print("not found")
else:
    print("position = ", result+1)
def contains(lst, x):
    for y in lst:
        if x == y: return True
    return False
ns = np.linspace(10, 10_000, 100, dtype=int)
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-r')
ts = [timeit.timeit('contains(lst, -1)', 
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=100)
      for n in ns]
plt.plot(ns, ts, 'ob')
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')