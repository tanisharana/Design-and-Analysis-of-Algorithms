import random 
import time 
import matplotlib.pyplot as plt
import timeit
def MergeSort(lst):
    if len(lst) > 1:
        middle = len(lst)//2
        l = lst[:middle]
        r = lst[middle:]
        
        MergeSort(l)
        MergeSort(r)
        
        i,j,k = 0,0,0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k]=l[i]
                i+=1
            else:
                lst[k]=r[j]
                j+=1
            k+=1
            
        while i < len(l):
            lst[k]=l[i]
            i+=1
            k+=1
                 
        while j < len(r):
            lst[k]=r[j]
            j+=1
            k+=1
            
    return lst

lst=[]
print("enter array size")
n=int(input())
print("enter array to be sorted")
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
                
print("sorted array is 2",MergeSort(lst))
N = 17
A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)
figure, ax = plt.subplots(figsize=(12,9))
bar_list = ax.bar(range(len(A)), A, width=0.3, align="edge", color="red")
index=count()
def update_figure(A, bars, iteration):
  for bar, value in zip(bars, A):
    bar.set_height(value)
        
  anim = FuncAnimation(figure, func=update_figure,
  fargs=(bar_list, next(index)), frames=MergeSort(A), interval=100,
  repeat=False,save_count=150)
plt.show()