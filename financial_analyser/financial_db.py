import sqlite3


class FinancialDb:
    """"Allows to perform CRUD operations"""

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS expenses_record (
            item_name text, 
            item_price float, 
            purchase_date date)""")
        self.con.commit()

    def create_record(self, item_name, item_price, purchase_date):
        """Allows to add data to the database"""
        self.cur.execute("INSERT INTO expenses_record VALUES (?, ?, ?)",
                         (item_name, item_price, purchase_date))
        self.con.commit()

    def read_record(self, query):
        """Allows to query the database"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def update_record(self, item_name, item_price, purchase_date, row_id):
        """Allows to update data from the database"""
        self.cur.execute(
            """UPDATE expenses_record SET item_name = ?, item_price = ?,
            purchase_date = ? WHERE rowid = ?""",
            (item_name, item_price, purchase_date, row_id))
        self.con.commit()

    def delete_record(self, row_id):
        """Allows to delete data from the database"""
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (row_id,))
        self.con.commit()

    def __del__(self):
        self.con.close()
