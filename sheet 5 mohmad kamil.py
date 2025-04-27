#1
list(range(6))
list(range(4, 11, 2))
list(range(10, 5, -1))
list(range(10, -11, -5))


#2
answer: [(1, 2, 0), (2, 4, -1), (3, 6, -2), (4, 8, -3), (5, 10, -4)]


#3
answer=[2, 3, 4]

def add_1(s):
    return s + 1
r = list(map(add_1, [1, 2, 3]))
print(r)


#4
def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

add_1 = lambda num: num + 1

r = apply([1, 2, 3], add_1)
print(r)



#5
answer:[10, 20, 30]
0


#6
x = [9,10,88,99]

print([True if num % 2 == 0 else False for num in x])


#7
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add(self, p):
        self.x += p.x
        self.y += p.y
        self.z += p.z

    def subtract(self, p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z

    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        delta_z = self.y - p.z

        dist = (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5
        return dist