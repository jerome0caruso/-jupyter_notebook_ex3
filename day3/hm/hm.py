# exercise #1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

filtered = list(filter(lambda place: len(place) > 2, places))
print("option #1", filtered)

    # option #2
def my_func(place):
    if len(place) > 2:
        return(place)
filtered2 = list(filter(my_func, places))
print("option #2", filtered2)

# excercise # 2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

print(sorted(author, key=lambda name: name.lower().split(" ")[-1]))


# exercise # 3
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]

mappeded = list(map(lambda temp: (9/5)*temp[1] + 32 , places))
print(mappeded)

# ** another option with city names
converted_places =  list(map(lambda x: (x[0], x[1] *(9/5) + 32) , places ))

#excercise # 4
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for n in range(1, 6):
    print(fib(n))
