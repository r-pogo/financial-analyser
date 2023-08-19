import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter import messagebox

from financial_db import *

# ---------------------------- UI SETUP ------------------------------- #

# Main window
window = tk.Tk()
window.title('Financial Analyser')
window.geometry('800x600+350+100')

# Global var for GUI
font = ('Times new roman', 11)
amount_var = tk.IntVar()
date_var = tk.StringVar()

# Frame widgets
"""Two main frames, one for treeview, one for operations"""
tree_scrollbar = ttk.Frame(window)
tree_scrollbar.pack()

operation_widgets = tk.Frame(window, padx=10, pady=10, )
operation_widgets.pack(expand=True, fill=tk.BOTH)

# Label Widget
"""Definition of labels fo input data"""
tk.Label(operation_widgets, text='EXPENSE', font=font).grid(row=0, column=0,
                                                            sticky=tk.W)
tk.Label(operation_widgets, text='AMOUNT', font=font).grid(row=1, column=0,
                                                           sticky=tk.W)
tk.Label(operation_widgets, text='DATE', font=font).grid(row=2, column=0,
                                                         sticky=tk.W)

# Entry Widgets
"""Definition of input boxes"""
expense = tk.Entry(operation_widgets, font=font)
expense.grid(row=0, column=1, sticky=tk.EW, padx=(10, 0))

amount = tk.Entry(operation_widgets, font=font, textvariable=amount_var)
amount.grid(row=1, column=1, sticky=tk.EW, padx=(10, 0))

date = tk.Entry(operation_widgets, font=font, textvariable=date_var)
date.grid(row=2, column=1, sticky=tk.EW, padx=(10, 0))

# Buttons
"""Definition of action buttons"""
cur_date_btn = tk.Button(operation_widgets, text='Current Date', font=font,
                     bg='#04C4D9', command=None, width=15)
cur_date_btn.grid(row=3, column=1, sticky=tk.EW, padx=(10, 0))

save_btn = tk.Button(operation_widgets, text='Save Record', font=font,
                     command=None, bg='#228B22', fg='white')
save_btn.grid(row=0, column=2, sticky=tk.EW, padx=(10, 0))

clear_btn = tk.Button(operation_widgets, text='Clear Entry', font=font,
                      command=None, bg='#D9B036', fg='white')
clear_btn.grid(row=1, column=2, sticky=tk.EW, padx=(10, 0))

import_btn = tk.Button(operation_widgets, text='Import File', font=font,
                       command=None, bg='#D9B036', fg='white')
import_btn.grid(row=1, column=4, sticky=tk.EW, padx=(10, 0))

exit_btn = tk.Button(operation_widgets, text='Exit', font=font, command=None,
                     bg='#D33532', fg='white')
exit_btn.grid(row=2, column=2, sticky=tk.EW, padx=(10, 0))

total_bal_btn = tk.Button(operation_widgets, text='Total Balance', font=font,
                          bg='#486966', fg='white', command=None)
total_bal_btn.grid(row=0, column=3, sticky=tk.EW, padx=(10, 0))

total_spent_btn = tk.Button(operation_widgets, text='Total Spent', font=font,
                            bg='#486966', fg='white', command=None)
total_spent_btn.grid(row=0, column=4, sticky=tk.EW, padx=(10, 0))

update_btn = tk.Button(operation_widgets, text='Update', font=font,
                       bg='#C2BB00', fg='white', command=None)
update_btn.grid(row=1, column=3, sticky=tk.EW, padx=(10, 0))

delete_btn = tk.Button(operation_widgets, text='Delete', font=font,
                       bg='#BD2A2E', fg='white', command=None)
delete_btn.grid(row=2, column=3, sticky=tk.EW, padx=(10, 0))
window.mainloop()
