class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def show(self):
        print(f'Point({self.x}, {self.y})')


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)
        
    def show(self):
        print(f'Rectangle: left-top {self.lt.get()}, right-bottom {self.rb.get()}')
        
    def getWidth(self):
        return self.rb.x - self.lt.x
    
    def getHeight(self):
        return self.rb.y - self.lt.y
    
    def getArea(self):
        return self.getWidth() * self.getHeight()
    
    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())


def test():
    p1 = Point()
    p2 = Point(2, 3)
    p1.show()
    p1.set(10, 20)
    p1.show()
    p2.show()
    x, y = p2.get()
    print(f'x={x}, y={y}')

# 주 프로그램부
if __name__ == '__main__':
    test()
    
    # 사각형 테스트
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()
    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')
