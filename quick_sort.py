import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

def partition(array, low, high):

  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1

      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)


data = [20,40,7.1,65,80,91,1,2]
print("Unsorted Array")
print(data)
size = len(data)

quickSort(data, 0, size - 1)
print('array after sorting')
print(data)
if __name__ == "__main__":

    N = 25
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)
    generator = quickSort(A, 0, N-1)

    figure, ax = plt.subplots(figsize=(19,15))
    bar_rects = ax.bar(range(len(A)), A, width=0.3, align="edge", color="green")

    
    iteration = [0]
    def update_figure(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1

        
    anim = FuncAnimation(figure, func=update_figure,
        fargs=(bar_rects, iteration), frames=generator, interval=100,
        repeat=False)
    plt.show()