'''
Author:    Emma Li
Program:   Gui.py
Date:      05/04/2020
Descr:
I am using pygame (1.9.6 Version), this is a menu file (tkinter).
'''

import tkinter as tk
import tkinter.messagebox as tkm
import Pong


class MyGUI:
    def __init__(self):
        # create main window
        self.main_window = tk.Tk()
        self.main_window.title('Pong Game')
        self.main_window.geometry('600x350')
        self.radio_var = tk.IntVar()
        self.radio_var2 = tk.IntVar()

        # create frame to hold name
        self.info_frame = tk.Frame(self.main_window, cursor='tcross')
        # setup grid properties for frame
        self.info_frame.grid(row=0, column=0, rowspan=3, columnspan=3)

        # create label and entry for name
        self.name1_label = tk.Label(self.info_frame, text='Player1 Name:')
        self.name1_entry = tk.Entry(self.info_frame, width=20)
        self.name2_label = tk.Label(self.info_frame, text='Player2 Name:')
        self.name2_entry = tk.Entry(self.info_frame, width=20)

        self.player1_label = tk.Label(self.main_window, text='Player 1:')
        self.player2_label = tk.Label(self.main_window, text='Player 2:')

        self.female1_radio = tk.Radiobutton(self.main_window,
                                            text='Female',
                                            variable=self.radio_var, value=1)

        self.male1_radio = tk.Radiobutton(self.main_window,
                                          text='Male',
                                          variable=self.radio_var, value=2)
        self.female2_radio = tk.Radiobutton(self.main_window,
                                            text='Female',
                                            variable=self.radio_var2, value=1)

        self.male2_radio = tk.Radiobutton(self.main_window,
                                          text='Male',
                                          variable=self.radio_var2, value=2)

        self.text_box = tk.Text(self.main_window, height=2, width=45, foreground='red')

        # place widgets in grid
        self.name1_label.grid(row=0, column=0, padx=5, pady=6)
        self.name1_entry.grid(row=0, column=1, padx=5, pady=6)
        self.name2_label.grid(row=1, column=0, padx=35, pady=6)
        self.name2_entry.grid(row=1, column=1, padx=5, pady=6)
        self.text_box.grid(row=3, column=1, padx=20, pady=6)

        self.female1_radio.grid(row=7, column=0, padx=2, pady=2)
        self.male1_radio.grid(row=8, column=0, padx=2, pady=2)
        self.female2_radio.grid(row=7, column=1, padx=2, pady=2)
        self.male2_radio.grid(row=8, column=1, padx=2, pady=2)

        self.player1_label.grid(row=6, column=0)
        self.player2_label.grid(row=6, column=1)

        # create frame to hold buttons
        self.button_frame = tk.Frame(self.main_window)
        # create buttons
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_game)
        self.exit_button = tk.Button(self.button_frame, text='Exit', command=self.exit_app)

        # pack button into frame
        self.start_button.pack(side='left', padx=5)
        self.exit_button.pack(side='left', padx=55)

        # place frames into the window
        self.button_frame.place(relx=.5, rely=.8, anchor='s')
        self.text_box.insert(tk.INSERT, 'Player1 use "W" for up, "S" for down\nPlayer2 use "UP" key and "DOWN" key')

        # start event loop
        self.main_window.mainloop()

    def get_info(self):
        p1name = self.name1_entry.get()
        p1gender = self.radio_var.get()
        p2name = self.name2_entry.get()
        p2gender = self.radio_var2.get()
        player_data = [p1name, p1gender, p2name, p2gender]
        return player_data

    def start_game(self):
        player_data = self.get_info()
        self.main_window.destroy()
        Pong.main(player_data)

    def exit_app(self):
        '''method to exit the game '''
        print('exit button')
        # confirm user wishes to exit

        response = tkm.askyesno('Confirmation', 'Are you sure you want to exit?')
        if response == True:
            self.main_window.destroy()

        return


if __name__ == '__main__':
    mygui = MyGUI()

