#test
import mx.ODBC.Windows, mx.DateTime, pprint, csv

def get_records():
	nav = mx.ODBC.Windows.Connect('Nav4Test',user='ODBC',password='',clear_auto_commit=0)
	cursor = nav.cursor()
	sql = """SELECT
	No_,
	Name,
	Address,
	"Address 2",
	"Address 3",
	"Post Code",
	State,
	"Country/Region Code",
	"Phone No_",
	"Fax No_",
	State,
	"Salesperson Code",
	"Customer Disc_ Group",
	"Payment Terms Code",
	"Credit Limit (LCY)"
	FROM Customer"""
	cursor.execute(sql)
	
	rows = cursor.fetchmany(10)
	writer = csv.writer(open("c:\customer.csv", "wb"))
	writer.writerows(rows)
	print rows

def main():
	get_records()


main()
raw_input("\n\nPress the enter key to exit.")
