import requests

import pymysql

from pymysql import MySQLError

try:

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="currencyconverterdb"
    )

    print("Successfully connected to the database")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            from_currency VARCHAR(255),
            to_currency VARCHAR(255),
            amount DECIMAL(10, 2),
            converted_result DECIMAL(10, 4)
        )
        ''')

   
except MySQLError as e:

    print(f"Error: {e}")


from_currency = input("Enter from currency:")

to_currency = input("Enter to currency:")

amount = int(input("Enter amount:"))

BaseUrl = f"https://v6.exchangerate-api.com/v6/27fc268596f6e11309a199f3/pair/{from_currency}/{to_currency}/{amount}"
converted_result=0
try:
    
    response = requests.get(BaseUrl)

    result = response.json()

    converted_result = result['conversion_result']

    print(f'{amount} {from_currency} = {converted_result} {to_currency}')
    cursor.execute('''
            INSERT INTO rates (from_currency, to_currency, amount, converted_result)
            VALUES (%s, %s, %s, %s)
        ''', (from_currency, to_currency, amount, converted_result))
    

    conn.commit()
    print("Conversion rate saved to the database successfully!")

except:
    print("Please provide valid currency code")

