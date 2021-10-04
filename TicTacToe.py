import tkinter
import tkinter.messagebox
import tkinter.font
import random


class TicTacToe:

    def __init__(self):
        self.list = [["" for k in range(3)] for m in range(3)]
        self.previous_value = ''
        self.playing_with = False
        self.background_colour = True

    def playing_with_computer(self):
        self.playing_with = True

    def two_player(self):
        self.playing_with = False

    def computer_chance(self):
        """This feature is still not available"""
        global button
        for k in range(3):
            if self.list[k].count("X") == 2:
                for v in range(3):
                    if self.list[k][v] != "X":
                        button[(k*3)+v][0].set("O")
            elif self.list[k].count("O") == 2:
                for v in range(3):
                    if self.list[k][v] != "O":
                        button[(k*3)+v][0].set("X")
            elif self.list[0][k] == self.list[1][k] == self.list[2][k]:
                pass
            else:
                if self.list[0][k] == self.list[1][k] == "X" or self.list[2][k] == self.list[1][k] == "X" or self.list[0][k] == self.list[2][k] == "X":
                    for v in range(3):
                        if self.list[v][k] != "X":
                            button[v*3+k][0].set("O")
                elif self.list[0][k] == self.list[1][k] == "O" or self.list[2][k] == self.list[1][k] == "O" or self.list[0][k] == self.list[2][k] == "O":
                    for v in range(3):
                        if self.list[v][k] != "O":
                            button[v*3+k][0].set("X")

                elif self.list[0][0] == self.list[2][2] == self.list[1][1] == "X":
                    for v in range(3):
                        if self.list[v][v] != "X":
                            # button[]
                            pass
                # if self.list[0][k].count("X") == 2:
            #     for v in range(3):
            #         if self.list[v][k] != "X":
            #             button[(k*3)+v+3][0].set("O")

    def check_score(self):
        """
        Checks after each chance if there is a winner and dilays a message if there is a winner.
        Also, if all the boxes have been filled, it checks for a tie as well.
        """
        val = 0
        for k in range(3):
            if self.list[k].count("X") == 3:
                tkinter.messagebox.showinfo(message="X Wins")
                self.new_game()
            elif self.list[k].count("O") == 3:
                tkinter.messagebox.showinfo(message="O Wins")
                self.new_game()
            else:
                rand = []
                for v in range(3):
                    rand.append(self.list[v][k])
                if rand.count("X") == 3:
                    tkinter.messagebox.showinfo(message="X Wins")
                    self.new_game()
                elif rand.count("O") == 3:
                    tkinter.messagebox.showinfo(message="O Wins")
                    self.new_game()
                elif self.list[0][0] == self.list[1][1] == self.list[2][2] == "X":
                    tkinter.messagebox.showinfo(message="X Wins")
                    self.new_game()
                elif self.list[0][0] == self.list[1][1] == self.list[2][2] == "O":
                    tkinter.messagebox.showinfo(message="O Wins")
                    self.new_game()
                elif self.list[0][2] == self.list[1][1] == self.list[2][0] == "X":
                    tkinter.messagebox.showinfo(message="X Wins")
                    self.new_game()
                elif self.list[0][2] == self.list[1][1] == self.list[2][0] == "O":
                    tkinter.messagebox.showinfo(message="O Wins")
                    self.new_game()
                elif self.list[k].count("X")+self.list[k].count("O") == 3:
                    val += 3
        if val == 9:
            tkinter.messagebox.showinfo(message="Its a Tie")
            self.new_game()

    def onclick(self, k, m, row_number):
        """
        Combines the tkinter buttons with events.
        :param k:row number of the tkinter button
        :param m:column number of the tkinter button
        :param row_number:the index position containing the row of the tkinter button in `button`
        :return: None
        """
        global button
        if self.list[k][m] == "":
            if self.previous_value == "":
                if self.previous_value == "":
                    self.previous_value = "X"
                    self.list[k][m] = "X"
                    button[row_number][0].set("X")
            else:
                if self.previous_value == "X":
                    button[row_number][0].set("O")
                    self.list[k][m] = "O"
                    self.previous_value = "O"
                else:
                    button[row_number][0].set("X")
                    self.list[k][m] = "X"
                    self.previous_value = "X"

            if self.playing_with:
                self.computer_chance()
            else:
                if self.previous_value == "X":
                    button[row_number][2].config(background="Yellow")
                    self.background_colour = False
                else:
                    button[row_number][2].config(background="Orange")
                    self.background_colour = True

        self.check_score()

    def new_game(self):
        """
        Starts a new game resetting all the parameters to its initial state
        """
        global button
        try:
            self.list = [["" for k in range(3)] for m in range(3)]
            self.previous_value = ''
            for k in range(9):
                button[k][0].set("")
            for m in range(9):
                button[m][2].config(background="blue")
        except:
            pass


if __name__ == '__main__':
    main_window = tkinter.Tk()
    main_window.geometry("520x560+350+100")
    main_window.title("Tic\tTac\tToe")
    main_window.config(padx="4", pady="4")
    main_window.maxsize(1000, 1000)
    main_window.minsize(500, 560)

    font = tkinter.font.Font(font='TkHeadingFont', weight="ITALIC")
    frame = tkinter.Frame()

    TicTacToe_command = TicTacToe()

    a = tkinter.StringVar()
    b = tkinter.StringVar()
    c = tkinter.StringVar()
    d = tkinter.StringVar()
    e = tkinter.StringVar()
    f = tkinter.StringVar()
    g = tkinter.StringVar()
    h = tkinter.StringVar()
    i = tkinter.StringVar()
    button = [
              [a, TicTacToe_command],
              [b, TicTacToe_command],
              [c, TicTacToe_command],
              [d, TicTacToe_command],
              [e, TicTacToe_command],
              [f, TicTacToe_command],
              [g, TicTacToe_command],
              [h, TicTacToe_command],
              [i, TicTacToe_command],
              ]

    row = 0
    for i in range(3):
        for j in range(3):
            value, command = button[row]
            button1 = tkinter.Button(frame, relief='raised', height=5, width=10, bg="white",
                                     textvariable=value,
                                     activebackground="green", background='blue',
                                     font=(font, 20), command=lambda val=row, y=i, z=j: command.onclick(y, z, val))
            button[row].append(button1)
            button1.grid(row=i, column=j, sticky='nsew')
            row += 1

    frame.grid(row=0, column=0)

    # play_with_computer_button = tkinter.Button(frame, text="Play with Computer",
    #                                            activebackground="blue", background='light green',
    #                                            command=TicTacToe_command.playing_with_computer)
    # play_with_computer_button.grid(row=0, column=4, padx=10, sticky='nsew')

    two_player_button = tkinter.Button(frame, text="Two Player",
                                       activebackground="blue", background='light green',
                                       command=TicTacToe_command.two_player)
    two_player_button.grid(row=1, column=4, padx=10, sticky='nsew')

    new_game_button = tkinter.Button(frame, text="New game",
                                     activebackground="blue", background='light green',
                                     command=TicTacToe_command.new_game)
    new_game_button.grid(row=2, column=4, padx=10, sticky='nsew')

    main_window.mainloop()
