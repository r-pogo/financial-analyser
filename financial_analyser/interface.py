import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter import messagebox

from financial_db import *

# ---------------------------- UI SETUP ------------------------------- #

# Main window
FONT = ('Times new roman', 11)
window = tk.Tk()
window.title('Financial Analyser')
window.geometry('800x600+350+100')

# Global var for GUI
amount_var = tk.IntVar()
date_var = tk.StringVar()

# Frame widgets
"""Two main frames, one for treeview, one for operations"""
tree_scrollbar = tk.Frame(window)
tree_scrollbar.pack()
# tree_scrollbar.grid(row=0, column=0,columnspan=2, padx=10, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)

operation_widgets = tk.Frame(window, padx=10, pady=10, )
operation_widgets.pack(expand=True, fill=tk.BOTH)
#operation_widgets.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

#####################
# operation_widgets #
#####################

# Label Widget
tk.Label(operation_widgets, text='EXPENSE', font=FONT).grid(row=0, column=0,
                                                             sticky=tk.W)
tk.Label(operation_widgets, text='AMOUNT', font=FONT).grid(row=1, column=0,
                                                            sticky=tk.W)
tk.Label(operation_widgets, text='DATE', font=FONT).grid(row=2, column=0,
                                                          sticky=tk.W)

# Entry Widgets
expense = tk.Entry(operation_widgets, font=FONT)
expense.grid(row=0, column=1, sticky=tk.EW, padx=(10, 0))

amount = tk.Entry(operation_widgets, font=FONT, textvariable=amount_var)
amount.grid(row=1, column=1, sticky=tk.EW, padx=(10, 0))

date = tk.Entry(operation_widgets, font=FONT, textvariable=date_var)
date.grid(row=2, column=1, sticky=tk.EW, padx=(10, 0))

# Buttons
cur_date_btn = tk.Button(operation_widgets, text='Current Date', font=FONT,
                         bg='#04C4D9', command=None, width=15)
cur_date_btn.grid(row=3, column=1, sticky=tk.EW, padx=(10, 0))

save_btn = tk.Button(operation_widgets, text='Save Record', font=FONT,
                     command=None, bg='#228B22', fg='white')
save_btn.grid(row=0, column=2, sticky=tk.EW, padx=(10, 0))

clear_btn = tk.Button(operation_widgets, text='Clear Entry', font=FONT,
                      command=None, bg='#D9B036', fg='white')
clear_btn.grid(row=1, column=2, sticky=tk.EW, padx=(10, 0))

import_btn = tk.Button(operation_widgets, text='Import File', font=FONT,
                       command=None, bg='#D9B036', fg='white')
import_btn.grid(row=1, column=4, sticky=tk.EW, padx=(10, 0))

exit_btn = tk.Button(operation_widgets, text='Exit', font=FONT, command=None,
                     bg='#D33532', fg='white')
exit_btn.grid(row=2, column=2, sticky=tk.EW, padx=(10, 0))

total_bal_btn = tk.Button(operation_widgets, text='Total Balance', font=FONT,
                          bg='#486966', fg='white', command=None)
total_bal_btn.grid(row=0, column=3, sticky=tk.EW, padx=(10, 0))

total_spent_btn = tk.Button(operation_widgets, text='Total Spent', font=FONT,
                            bg='#486966', fg='white', command=None)
total_spent_btn.grid(row=0, column=4, sticky=tk.EW, padx=(10, 0))

update_btn = tk.Button(operation_widgets, text='Update', font=FONT,
                       bg='#C2BB00', fg='white', command=None)
update_btn.grid(row=1, column=3, sticky=tk.EW, padx=(10, 0))

delete_btn = tk.Button(operation_widgets, text='Delete', font=FONT,
                       bg='#BD2A2E', fg='white', command=None)
delete_btn.grid(row=2, column=3, sticky=tk.EW, padx=(10, 0))

chart_btn = tk.Button(operation_widgets, text='Visualize Data', font=FONT,
                      bg='#BD2A2E', fg='white', command=None)
chart_btn.grid(row=2, column=4, sticky=tk.EW, padx=(10, 0))

##################
# tree_scrollbar #
##################

# Treeview
treeview = ttk.Treeview(tree_scrollbar, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8, )
treeview.pack(side="left")

treeview.column(1, anchor=tk.CENTER, stretch=tk.NO, width=70)
treeview.column(2, anchor=tk.CENTER)
treeview.column(3, anchor=tk.CENTER)
treeview.column(4, anchor=tk.CENTER)
treeview.heading(1, text="Serial no")
treeview.heading(2, text="Expense", )
treeview.heading(3, text="Amount")
treeview.heading(4, text="Date")

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

# Scrollbar
scrollbar = tk.Scrollbar(tree_scrollbar, orient='vertical')
scrollbar.configure(command=treeview.yview)
scrollbar.pack(side="right", fill="y")
treeview.config(yscrollcommand=scrollbar.set)

########
# Menu #
########

menu = tk.Menu(window)
window.configure(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Menu', menu=file_menu)
file_menu.add_command(label='Open file') #command=open_file)
#file_menu.add_command(label='Save', command=save)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=window.destroy)

# Options
options_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Options', menu=options_menu)
#options_menu.add_checkbutton(label='Private', variable=private_var)

# Help menu
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label='About',
                      command=lambda: messagebox.showinfo('About', '#TODO'))
menu.add_cascade(label='Help', menu=help_menu)

# Chart menu
visualize_data_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Visualize Data', menu=visualize_data_menu)

charts_menu = tk.Menu(visualize_data_menu, tearoff=0)
visualize_data_menu.add_cascade(menu=charts_menu, label='Charts')

charts = ['Pie', 'Scatter plot', 'Histogram', 'Line chart', 'Bar chart']

for chart in charts:
    charts_menu.add_radiobutton(
        label=chart,
        value=chart,
        # variable= zrobic zmienna ktora bedzie aplikowala rozne wykresy
    )

window.mainloop()
