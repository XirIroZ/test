import tkinter as tk
from tkinter import messagebox 
import sqlite3
from datetime import datetime
from tkinter import ttk


messagebox.showinfo("Information", "Bienvenue dans votre planificateur de tâche !")

splash_screen = tk.Tk()
splash_screen.title("Xeno IROZ 🐦‍🔥 : Lancement de la ToDoList")

splash_screen.geometry("620x400+500+200")


label4 = tk.Label(splash_screen, text = "TODOLIST", font = ("Verdana", 50))
label4.pack(expand = "True")


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS Finals(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Tache TEXT NOT NULL,
                   Date_de_création TEXT NOT NULL,
                   Priorité TEXT NOT NULL,
                   Date_de_réalisation TEXT NOT NULL,
                   Statut TEXT NOT NULL
                   
    )""")
conn.commit()
conn.close()

from PIL import Image, ImageTk

image = Image.open(r"C:\Users\Emmanuel BANIZA\Downloads\v.jpg")
image = image.resize((620,400))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(label4,image = photo, bg ="gray")
image_label.photo = photo
image_label.pack(pady =10)

select = None
#Creation de la fenetre 
 
def ouverture():
    
    
    root = tk.Tk()
    root.config(bg = "gray")
    root.title ("Xeno 🐦‍🔥")
    root.geometry("800x900")
    


#Creation du label du titre de la fenetre
    label = tk.Label(root, text = "ToDoList 📝", font = ("Times New Roman", 10,"underline","italic"))
    label.config(bg = "gray")
    label.pack(pady = 10)

#Affichage de l'image
    from PIL import Image, ImageTk

    image = Image.open(r"C:\Users\Emmanuel BANIZA\Downloads\pngegg.png")
    image = image.resize((120,100))
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image = photo, bg ="gray")
    image_label.photo = photo
    image_label.pack(pady =10)



#Creation du cadre
    cadre = tk.Frame(root, bd = 2, relief = "solid")
    cadre.pack(padx=15, pady=15, fill="both", expand="True")

#Creation des labels et champs d'ajout de taches  
    label_2 = tk.Label(cadre, font = ("Times New Roman", 10)) 
    label_2.pack()
    

    label = tk.Label(root, font = ("Times New Roman", 10))
    DESCRIPTION = tk.Label(root, text = "Tache :", font = ("Comic Sans MS", 10),relief = "ridge",bg ="gray")
    DESCRIPTION.pack()
    DESCRIPTION.config(bg = "gray")
    Description = tk.Entry(root,  font = ("Times New Roman", 10))
    Description.pack()

    Priorité = ["Faible", "Intermédiaire", "Haute"]
    combo = ttk.Combobox(root, values = Priorité,font = ("Times New Roman", 10))
    combo.current(0)
    PRIORITE = tk.Label(root, text = "Priorité  :", font = ("comic sans MS", 10),relief = "ridge",bg ="gray")
    PRIORITE.pack(pady = 10)
    combo.pack()
    

    DATE = tk.Label(root, text = "Date de réalisation : ", font= ("comic sans MS", 10),relief = "ridge",bg ="gray" )
    DATE.pack(pady = 10)
    Date = tk.Entry(root,  font = ("Times New Roman", 10))
    Date.pack()
    
    
    
    STATUT = tk.Label(root,text = "Statut", font= ("comic sans MS", 10),relief = "ridge",bg ="gray")
    STATUT.pack(pady = 10)
    Statut = ["En Cours","Pas encore entamé", "Terminé"]
    combo1 = ttk.Combobox(root, values = Statut,font = ("Times New Roman", 10))
    combo1.current(0)
    combo1.pack()

#Initialisation de la ToDoList de base
    ToDoList = [{
    "Description" : "Faire semblant de bosser math",
    "Date de création" : "18-02-2025",
    "Priorité" : "Haute",
    "Date de réalisation" : "18-02-2025" ,
    "Statut" : "En Cours"
    
},
            {
    "Description" : "Jouer",
    "Date de création" : "20-02-2025",
    "Priorité" : "Moyenne",
    "Date de réalisation" : "20-02-2025",
    "Statut" : "Fait"
    
}
             
   ]

#Création du label d'affichage de message d'erreur 

    
    
    def affichage():
    
        for widget in cadre.winfo_children() :
            if type(widget) == tk.Label and widget != label_2 :
                widget.destroy()
    
        
        for i,  element in enumerate(ToDoList) :
        
            texte = f"Tache : {element['Description']}\n Date de création : {element['Date de création']}\n Priorité : {element['Priorité']}\n Date de réalisation : {element['Date de réalisation']}\n Statut : {element['Statut']} "  
         
            label = tk.Label(cadre, text = texte, font = ("Helvetica", 9,"italic"))
            label.pack()
         
            label.bind("<Button-1>", lambda event, idx= i: selection(idx))
            label.bind("<Button-2>", lambda event, idx= i: selection(idx))
            label.bind("<Button-3>", lambda event, idx= i: selection(idx))
        
    
    def ajouter():
        description = Description.get()
        priorité = combo.get()
        date = Date.get()
        statut = combo1.get()
        date_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if description and priorité and  date and statut :
            Tache = {
    "Description" : description,
    "Date de création" : date_creation,
    "Priorité" : priorité,
    "Date de réalisation" : date,
    "Statut" : statut} 

            ToDoList.append(Tache)
            affichage()
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Finals (Tache,Date_de_création,Priorité, Date_de_réalisation,Statut) VALUES(?,?,?,?,?)",(description,date_creation,priorité,date,statut)) 
            conn.commit()   
            conn.close()
        else:
            messagebox.showwarning("Information", "Champs obligatoires !")
  
            
    def selection(index):
        global select 
        for widget in cadre.winfo_children():
            if type(widget) == tk.Label and widget != label_2:
                widget.config(bg ="white")
        select = index
        cadre.winfo_children()[index+1].config(bg="lightblue")
                 
    def supprimer():
        description = Description.get()
        priorité = combo.get()
        date = Date.get()
        statut = combo1.get()
        
        global select

        if select is not None:
            
            del ToDoList[select]
            select = None  
            affichage()
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Finals WHERE Tache = ?  AND Priorité = ? AND Date_de_réalisation = ? AND Statut = ? ",(description,priorité,date,statut)) 
            conn.commit()   
            conn.close()
        else :
            
            messagebox.showerror("Erreur", "Sélectionnez une tâche à supprimer !")     

#Création et animation des boutons 

    bouton = tk.Button(root, text = "Afficher la Todolist", font = ("Impact", 10), command = affichage, relief = "raised")
    bouton.config(bg="cyan")   
    bouton_2 = tk.Button(root, text = "Ajouter une tache", font = ("Impact", 10), relief = "raised",  command = lambda : ajouter())
    bouton_2.config(bg="green")   
    bouton_3 = tk.Button(root, text = "Supprimer une tache", font = ("Impact", 10), relief = "raised", command =  lambda : supprimer() )
    bouton_3.config(bg="red")   
    bouton.pack(pady = 10)
    bouton_2.pack(pady = 10)
    bouton_3.pack(pady = 10)
    bouton_fermer = tk.Button(root, text = "Quitter", font = ("Impact", 10), command = lambda : fermer(), relief = "raised" )
    bouton_fermer.config(bg ="red")
    bouton_fermer.pack(pady = 10)
 
    def fermer():
        reponse = messagebox.askquestion(title="Information", message="Voulez-vous continuer ?")
        print(reponse)
        if reponse == "yes" :                                                                           
            root.destroy()

    root.mainloop()

#Affichage du message d'au revoir
    messagebox.showinfo("Information", "Au revoir !")
def fermeture():
    splash_screen.destroy()
    ouverture()
splash_screen.after(3000, fermeture)

splash_screen.mainloop()


