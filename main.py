from vector import Vector

if __name__ == '__main__':
    vector_list = [Vector(5, 2, -3, 8),
                   Vector(4, 1, 3, 9),
                   Vector(-2, -2, 8, 8)]
    for vector in vector_list:
        print(vector.length())