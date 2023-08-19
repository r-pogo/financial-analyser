import sqlite3


class FinancialDb:
    """"Allows to perform CRUD operations"""

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS expenses_record (
            expense text, 
            amount float, 
            date date)""")
        self.con.commit()

    def create_record(self, expense, amount, date):
        """Allows to add data to the database"""
        self.cur.execute("INSERT INTO expenses_record VALUES (?, ?, ?)",
                         (expense, amount, date))
        self.con.commit()

    def read_record(self, query):
        """Allows to query the database"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def update_record(self, expense, amount, date, row_id):
        """Allows to update data from the database"""
        self.cur.execute(
            """UPDATE expenses_record SET expense = ?, amount = ?,
            date = ? WHERE rowid = ?""",
            (expense, amount, date, row_id))
        self.con.commit()

    def delete_record(self, row_id):
        """Allows to delete data from the database"""
        self.cur.execute("DELETE FROM expenses_record WHERE rowid=?", (row_id,))
        self.con.commit()

    def __del__(self):
        self.con.close()
