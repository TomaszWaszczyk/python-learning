import tkinter

# w tej wersji oprócz kliknięcia guzika obsłużymy także naciśnięcie enter gdy jesteśmy w polu tekstowym

def main():
    global poleTekstowe, label2

    root = tkinter.Tk()

    root.title('Rozmowa')
    root.geometry('800x600')

    label1 = tkinter.Label(master=root, text='Jak masz na imię?', fg='black', font=('Arial', 24, 'bold'))
    label1.pack()

    poleTekstowe = tkinter.Entry(root, font=('Consolas', 24), bg='white')
    poleTekstowe.pack()

    button1 = tkinter.Button(master=root, text='OK', font=('Arial', 24, 'bold'))
    button1.pack()

    label2 = tkinter.Label(master=root, text='', fg='blue', font=('Arial', 24, 'bold'))
    label2.pack()

    # ustawiam obsługę zdarzenia "kliknięcie guzika"
    button1.configure(command=lambda: label2.configure(text=f'Witaj {poleTekstowe.get()}!'))

    # aby dodać obsługę zdarzenia dla pola tekstowego, trzeba zastosować ogólną technikę "bind"
    poleTekstowe.bind('<Return>', lambda event: label2.configure(text=f'Witaj {poleTekstowe.get()}!'))

    root.mainloop()

if __name__ == '__main__':
    main()
