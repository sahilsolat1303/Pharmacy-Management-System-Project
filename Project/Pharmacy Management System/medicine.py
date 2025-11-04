class Medicine:
    def __init__(self, medicine_id, name, type, price, quanitity):
        self.m_id = medicine_id
        self.nm = name
        self.type = type
        self.price = price
        self.quanitity = quanitity
        

    
    def show(self):
        print("Medicine_ID:",self.m_id)
        print("Name:",self.nm)
        print("Type:",self.type)
        print("Price:",self.price)
        print("Quantity:",self.quanitity)
        
    

    def __str__(self):
        return f'{self.m_id}, {self.nm}, {self.type}, {self.price}, {self.quanitity}'



if __name__ == '__main__':
    m1 = Medicine('M100', 'Paracetamol', 'Tablet', 25, 100)
    m1.show()