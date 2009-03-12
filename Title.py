import mx.ODBC.Windows, mx.DateTime, pprint, csv

def get_records():
	nav = mx.ODBC.Windows.Connect('Nav4Test',user='ODBC',password='',clear_auto_commit=0)
	cursor = nav.cursor()
	sql = """SELECT
	"Inventory Posting Group",
	"Gen_ Prod_ Posting Group",
	"Publisher Code",
	APN,
	ISBN,
	Binding,
	Title,
	"Item Disc_ Group",
	Blocked,
	"Unit Cost",
	"Net Weight",
	"Return Rights",
	"Length (mm)",
	"Width (mm)",
	"Publication Date"
	FROM Item"""
	cursor.execute(sql)
	
	rows = cursor.fetchmany(10)
	writer = csv.writer(open("c:\GET_RECORDS.csv", "wb"))
	writer.writerows(rows)
	print rows

def main():
	get_records()


main()

raw_input("\n\nPress the enter key to exit.")
