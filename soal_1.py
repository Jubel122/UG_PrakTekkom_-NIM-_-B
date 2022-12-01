print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
def add (): 
    c = a + b  
    print("hasil pemjumlahan",c)
a = (int(input("masukkan angka a>> " )))
b = (int(input("masukkan angka b>> ")))
c()

def subtract ():
    c = a * b
    print ("hasil pembagian",c)
a = (int(input("masukkan angka a>> " )))
b = (int(input("masukkan angka b>> ")))   
c() 

def multiply ():
    c = a / b
    print("hasil perkalian",c )
a = (int(input("masukkan angka a>> " )))
b = (int(input("masukkan angka b>> ")))
c()

def divide():
    c = a - b 
    print("hasil pengurangan",c )
a = (int(input("masukkan angka a>> " )))
b = (int(input("masukkan angka b>> ")))
c()
