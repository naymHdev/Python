""" Lecture - 3 """
""" List in python """

marks = [12, 232, 33, 222, 321, 2321, 212]
# print(type(marks), marks)

student = ['naym', 'dhaka', 'student', 'find job', 20000, 23]
# print("student: ", student)

# Python "String" are immutable but python list ["String"] are mutable.
# Like
jon = ['marker', 2356, 'hitler']
# print(jon)
jon[0] = 'tailor'
# print(jon)


# List Slicing like of String Slicing

trailer = ['marker', 2356, 'hitler', 32765, 232, 323, 323, 2]
listSlice = trailer[2:5]
# print("listSlice: ", listSlice)


# List's Methods are

listNum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listNum.append(10)
# print(listNum)

checkShort = [1, 3, 2, 8, 3, 0, 4, 12, 333, 22, 11]
# checkShort.sort(reverse=True)
# checkShort.sort()
# checkShort.reverse()
# checkShort.insert(3, 99)
# checkShort.remove(1)
# checkShort.pop(0)
# print(checkShort)


""" Tuples in Python """

tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(type(tup))
# print(tup)


""" Let's Practice """

# 1. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movieCollection = []
movie1 = input('Movie name: ')
movie2 = input('Movie name: ')
movie3 = input('Movie name: ')

movies = movie1, movie2, movie3
movieCollection.append(movies)
print("movieCollection: ", movieCollection)

# 2. WAP to count the number of students with the “A” grade in the following tuple.
# solved !!