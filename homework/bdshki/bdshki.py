import sqlite3

cust = str(8)
db = "base.sqlite"
connection = sqlite3.connect(db)
cursor = connection.cursor()
cursor.execute('''SELECT Name FROM Track 
                LEFT JOIN 'InvoiceLine' ON InvoiceLine.TrackId=Track.TrackId 
                LEFT JOIN 'Invoice' ON InvoiceLine.InvoiceId=Invoice.InvoiceId WHERE CustomerId = ''' + cust)

ress = cursor.fetchall()

for res in ress:
    print(str(res)[1:-1])