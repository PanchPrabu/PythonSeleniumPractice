# ExceptionsHandlinginPython

ItemsInCart =0

#if ItemsInCart!=2 :
    #raise Exception("ProductsCartcountnotmatches")

#assert(ItemsInCart==2)

try:
    with open('testing.txt','r') as R1:
        R1.read()
except:
    print("I am handling the try except scenarios")

try:
    with open('testing123.txt', 'r') as R1:
        R1.read()

except Exception as e:
        print(e)

finally:
    print("cleaning up your data")






