class User:
    def __init__(self, id, name, address):
        self.eid = id
        self.ename = name
        self.add = address

    
    def __str__(self):
        return f'{self.eid}, {self.ename}, {self.add}'
    
if __name__ == '__main__':
    e1 = User(101, 'sahil', 20000)
    print(e1)