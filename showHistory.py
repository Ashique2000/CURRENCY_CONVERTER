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
      SELECT * FROM rates;
        ''')
    
    rows = cursor.fetchall()

    # Print table headers
    print(f"{'SL.NO':<5} {'From currency':<15} {'To currency':<15} {'Amount':<10} {'Conversion Rate':<15}")

    # Loop through the rows and print each record
    for row in rows:
        id, from_currency, to_currency, amount, converted_result = row
        print(f"{id:<5} {from_currency:<15} {to_currency:<15} {amount:<10} {converted_result:<15}")


    
    

except MySQLError as e:

    print(f"Error: {e}")


