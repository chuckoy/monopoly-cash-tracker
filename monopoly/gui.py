from tkinter import *
from tkinter import ttk
from functools import partial

from errors import InputError


class GUI:

    def __init__(self, game):
        # Initialise needed variables
        self.game = game
        self.no_dot = True
        self.payment_flag = False

        # Create window
        self.root = Tk()
        self.root.title("Monopoly Calculator")
        self.root.resizable(FALSE, FALSE)

        # Create main frame
        self.main_frame = ttk.Frame(self.root, borderwidth=3, relief='raised')
        self.main_frame.grid(column=0, row=0, sticky=(N, S, E, W))

        # Create subframes
        # Make "dot matrix" subframe
        self.calc_matrix = ttk.Frame(
            self.main_frame, borderwidth=3, relief='sunken')
        self.calc_matrix.grid(column=0, row=0, sticky=(N, W, E))
        # Make button subframe
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(column=0, row=2, sticky=(S, W))
        # Make info panel subframe
        self.info_panel = ttk.Frame(
            self.main_frame, borderwidth=10, relief='sunken')
        self.info_panel.grid(column=2, row=0, rowspan=3, sticky=(N, E))

        # Create labels for player list
        self.player_list = ttk.Treeview(self.info_panel,
                                        columns=('money', 'pk'),
                                        displaycolumns=('money'),
                                        selectmode='browse')

        # Name the column headers
        self.player_list.heading('#0', text='Name')
        self.player_list.heading('money', text='Money')

        # Bind click event to set player change
        self.player_list.bind('<ButtonRelease-1>', self.player_clicked)

        # Populate tree
        self.draw_player_list()

        self.player_list.grid(column=0, row=0)

        # Create labels for input and quantifier
        self.number = StringVar()
        self.quantifier = StringVar()
        ttk.Label(self.calc_matrix, textvariable=self.number,
                  width=40, anchor=CENTER).grid(column=0, columnspan=3, row=0)
        ttk.Label(self.calc_matrix, textvariable=self.quantifier,
                  anchor=E).grid(column=2, row=0, sticky=E)

        # First row buttons
        (ttk
         .Button(self.button_frame, text="M",
                 command=partial(self.quantifier_input, "M"))
         .grid(column=0, row=1))
        (ttk
         .Button(self.button_frame, text="←", command=self.backspace)
         .grid(column=1, row=1))
        (ttk
         .Button(self.button_frame, text="K",
                 command=partial(self.quantifier_input, "K"))
         .grid(column=2, row=1))

        # Number grid
        for i in range(0, 3):
            for j in range(0, 3):
                value = str((3 * i) + j + 1)
                (ttk
                 .Button(self.button_frame, text=value,
                         command=partial(self.number_input, value))
                 .grid(column=j, row=i + 2))

        # After number grid row buttons
        (ttk
         .Button(self.button_frame, text="C", command=self.clear_calc)
         .grid(column=0, row=5))
        (ttk
         .Button(self.button_frame, text="0",
                 command=partial(self.number_input, "0"))
         .grid(column=1, row=5))
        (ttk
         .Button(self.button_frame, text=".", command=self.dot_input)
         .grid(column=2, row=5))

        # Bottom row buttons
        (ttk
         .Button(self.button_frame, text="+", command=self.plus_clicked)
         .grid(column=0, row=6))
        (ttk
         .Button(self.button_frame, text="+++", command=self.payment)
         .grid(column=1, row=6))
        (ttk
         .Button(self.button_frame, text="-", command=self.minus_clicked)
         .grid(column=2, row=6))

        # Configure button frame paddings
        for child in self.button_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Make keybindings

        # Number keybindings
        for i in range(0, 10):
            self.root.bind(str(i), partial(self.number_input, str(i)))
        # Dot bind
        self.root.bind('.', self.dot_input)
        # Clear calc binds
        self.root.bind('c', self.clear_calc)
        self.root.bind('C', self.clear_calc)
        # Quantifier binds
        self.root.bind('m', partial(self.quantifier_input, 'M'))
        self.root.bind('M', partial(self.quantifier_input, 'M'))
        self.root.bind('k', partial(self.quantifier_input, 'K'))
        self.root.bind('K', partial(self.quantifier_input, 'K'))
        # Backspace bind
        self.root.bind('<BackSpace>', self.backspace)
        # Payment binds
        self.root.bind('+', self.plus_clicked)
        self.root.bind('-', self.minus_clicked)
        self.root.bind('<space>', self.payment)

        self.root.mainloop()

    def number_input(self, *args):
        self.number.set(self.number.get() + args[0])

    def quantifier_input(self, *args):
        self.quantifier.set(args[0])

    def clear_calc(self, *args):
        self.number.set("")
        self.quantifier.set("")
        self.no_dot = True

    def dot_input(self, *args):
        if self.no_dot and self.number.get() != "":
            self.number_input(".")
            self.no_dot = False

    def backspace(self, *args):
        old_value = self.number.get()
        rest = old_value[:-1]
        self.number.set(rest)

    def plus_clicked(self, *args):
        if self.payment_flag:
            self.game.collect_pool_money(self.get_selected_player())
            self.update_player_list()
            self.payment_flag = False
        else:
            amount, quantifier = self.get_input()
            self.game.add_money(self.get_selected_player(), amount, quantifier)
            self.update_player_list()

    def payment(self, *args):
        self.payment_flag = True
        amount, quantifier = self.get_input()
        self.game.deduct_money(self.get_selected_player(), amount, quantifier)
        self.game.pool_money(amount, quantifier)
        self.update_player_list()

    def minus_clicked(self, *args):
        amount, quantifier = self.get_input()
        self.game.deduct_money(self.get_selected_player(), amount, quantifier)
        self.update_player_list()

    def get_selected_player(self):
        return self.player_list.focus()

    def update_player_list(self):
        for player in self.game.get_players():
            self.player_list.delete(player.get_name())
        self.draw_player_list()
        self.clear_calc()

    def draw_player_list(self):
        for player in self.game.get_players():
            self.player_list.insert('', 'end', player.get_name(),
                                    text=player.get_name(),
                                    values=(player.get_balance_display(),
                                            player.get_pk()),
                                    tags=(player.get_pk()))

    def get_input(self):
        amount = self.number.get()
        quantifier = self.quantifier.get()
        if quantifier == "":
            raise InputError("Place a valid quantifier!")
        return amount, quantifier
