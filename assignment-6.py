import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "rps@123", database = "kpmg")

mycursor = mydb.cursor()

def insert():
    product = int(input("Product ID : "))
    product_name = input("Product Name : ")
    product_price = int(input("Product Price : "))
    product_description = input("Product Description : ")
    product_category = input ("Product Category : ")
    mycursor.execute(f"INSERT INTO  products_info VALUES({product},'{product_name}',{product_price},'{product_description}','{product_category}')")
    mydb.commit()
    print("Data inserted successfully")

def update():
    product = int(input("Enter product Id for updating price : "))
    product_price = int(input("Enter updated Price : "))
    mycursor.execute(f"UPDATE products_info set productPrice = {product_price}  where productId = {product}" )
    mydb.commit()

def delete():
    product = int(input("Enter product Id for deleting data : "))
    mycursor.execute(f"DELETE FROM products_info where productId = {product}" )
    mydb.commit()

def display():
    product = int(input("Enter product Id to display data : "))
    mycursor.execute(f"SELECT * FROM  products_info where productId = {product}" )
    result = mycursor.fetchone()
    print(result)

def displayall():
    mycursor.execute("select * from products_info")
    data = mycursor.fetchall()
    for row in data:
        print("ProductID : ",row[0])
        print("Product Name : ",row[1])
        print("Product Price : ",row[2])
        print("Product Description : ",row[3])
        print("Product Category : ",row[4])

print("~~~Product Management~~~ \n 1. Add Product \n 2. Update Product \n 3. Delete ProductById \n 4. Get ProductById \n 5. Get All Products ")
option = int(input("Enter your option number : ")) 
if option == 1:
    insert()

elif option == 2:
    update()

elif option == 3:
    delete()

elif option == 4:
    display()
        
elif option == 5:
    displayall()

else:
    print("Invalid Option!! Try Again")
