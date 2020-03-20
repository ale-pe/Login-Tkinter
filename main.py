import sqlite3
from tkinter import *
from tkinter.messagebox import *


connection = sqlite3.connect('base.db')
cursor = connection.cursor()

# Code pour créer une base de donées
#cursor.execute('CREATE TABLE base (id TEXT, mdp TEXT)')
#cursor.execute('INSERT INTO base VALUES(?, ?)', ('admin','admin'))
#connection.commit()



def connect():
    print(IDF.get())
    donnee = (str(IDF.get()), )
    cursor.execute("SELECT * FROM base WHERE id = ?", donnee)
    row = cursor.fetchone()
    #print(row)
    if str(row) == "None":
        print(showerror("Erreur", "Aucun utilisateur trouvé")) 
    else :
        if str(row[1]) == str(MDPF.get()):
            userf = str(row[0])
            print(showinfo("Information", "Bonjour "+userf))
            F.destroy()
        else :
            print(showerror("Erreur", "Mot de passe incorrect")) 

   
def gg():
     id = row[0]
     name = row[1]
     print(str(id))
     print(str(name))
     print(str(row[4]))
     connection.commit()


F = Tk()
F.title('Caisse')
F['bg']='#40E0D0' # couleur de fond
connection.commit()
IDF= StringVar()
MDPF= StringVar()

F1 = Frame(F,bg="white",borderwidth=2,relief=GROOVE)
F1.pack(padx=10,pady=10)

F2 = Frame(F,bg="white",borderwidth=2,relief=GROOVE)
F2.pack(padx=10,pady=10)

Label(F1,text="User :",bg="white").pack(padx=10,pady=10)
Champ1 = Entry(F1, textvariable= IDF, bg ='bisque', fg='maroon')
Champ1.focus_set()
Champ1.pack(side = LEFT, padx = 5, pady = 5)
Label(F2,text="MDP :",bg="white").pack(padx=10,pady=10)
Champ = Entry(F2, textvariable= MDPF, show='*', bg ='bisque', fg='maroon')
Champ.pack(side = LEFT, padx = 5, pady = 5)
Button(F,text="Suivant",fg='navy',command=connect).pack(padx=10,pady=10)






