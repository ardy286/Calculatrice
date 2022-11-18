# Importation des librairies
import tkinter
import fonction_calculatrice

# Création de l'interface graphique
calculatrice = tkinter.Tk()

# Logo de l'application 
calculatrice.tk.call('wm','iconphoto',calculatrice._w,tkinter.PhotoImage(file="C:\\Users\\arist\\OneDrive\\Documents\\Calculatrice\\logoCalculatirce.png"))

# Nom et size de l'application
calculatrice.title("Ardy's calculatrice")
ecran_x = int(calculatrice.winfo_screenwidth())
ecran_y = int(calculatrice.winfo_screenheight())
ecranApp_x = 475
ecranApp_y = 600
pos_x = (ecran_x // 2) - (ecranApp_x // 2)
pos_y = (ecran_y // 2) - (ecranApp_y // 2)
geo = "{}x{}+{}+{}".format(ecranApp_x,ecranApp_y,pos_x,pos_y)
calculatrice.geometry(geo)
calculatrice.minsize(ecranApp_x,ecranApp_y)
calculatrice.maxsize(ecranApp_x,ecranApp_y)

#Variables
tab = []

#fontion    
def res():
    bada = tkinter.Label(calculatrice, text = "                      ",  font=("MADEAvenuePERSONALUSE-Regular",17))
    bada.place(relx = 0.50, rely = 0.710, anchor = "center")
    tab.append(numero.get())
    tab.append(numero1.get())
    tab.append(numero2.get())
    if(tab[0] == 1):
        resi = round(float(tab[1] + tab[2]),1)
        n1 = tkinter.Label(calculatrice, text = str(tab[1]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n1.place(relx = 0.42, rely = 0.710, anchor = "center")
        s = tkinter.Label(calculatrice, text = "+",  font=("MADEAvenuePERSONALUSE-Regular",15))
        s.place(relx = 0.47, rely = 0.710, anchor = "center")
        n2 = tkinter.Label(calculatrice, text = str(tab[2]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n2.place(relx = 0.52, rely = 0.710, anchor = "center")

        eg = tkinter.Label(calculatrice, text = "=",  font=("MADEAvenuePERSONALUSE-Regular",15))
        eg.place(relx = 0.55, rely = 0.710, anchor = "center")
        
        resu = tkinter.Label(calculatrice, text = str(resi),  font=("MADEAvenuePERSONALUSE-Regular",15))
        resu.place(relx = 0.60, rely = 0.710, anchor = "center")
    elif(tab[0] == 2):
        resi = round(float(tab[1] - tab[2]),1)
        n1 = tkinter.Label(calculatrice, text = str(tab[1]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n1.place(relx = 0.42, rely = 0.710, anchor = "center")
        s = tkinter.Label(calculatrice, text = "-",  font=("MADEAvenuePERSONALUSE-Regular",15))
        s.place(relx = 0.47, rely = 0.710, anchor = "center")
        n2 = tkinter.Label(calculatrice, text = str(tab[2]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n2.place(relx = 0.52, rely = 0.710, anchor = "center")

        eg = tkinter.Label(calculatrice, text = "=",  font=("MADEAvenuePERSONALUSE-Regular",15))
        eg.place(relx = 0.55, rely = 0.710, anchor = "center")
        
        resu = tkinter.Label(calculatrice, text = str(resi),  font=("MADEAvenuePERSONALUSE-Regular",15))
        resu.place(relx = 0.60, rely = 0.710, anchor = "center")
    elif(tab[0] == 3):
        resi = round(float(tab[1] * tab[2]),1)
        n1 = tkinter.Label(calculatrice, text = str(tab[1]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n1.place(relx = 0.42, rely = 0.710, anchor = "center")
        s = tkinter.Label(calculatrice, text = "x",  font=("MADEAvenuePERSONALUSE-Regular",15))
        s.place(relx = 0.47, rely = 0.710, anchor = "center")
        n2 = tkinter.Label(calculatrice, text = str(tab[2]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n2.place(relx = 0.52, rely = 0.710, anchor = "center")

        eg = tkinter.Label(calculatrice, text = "=",  font=("MADEAvenuePERSONALUSE-Regular",15))
        eg.place(relx = 0.55, rely = 0.710, anchor = "center")
        
        resu = tkinter.Label(calculatrice, text = str(resi),  font=("MADEAvenuePERSONALUSE-Regular",15))
        resu.place(relx = 0.60, rely = 0.710, anchor = "center")
    elif(tab[0] == 4):
        resi = round(float(tab[1] / tab[2]),1)
        n1 = tkinter.Label(calculatrice, text = str(tab[1]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n1.place(relx = 0.42, rely = 0.710, anchor = "center")
        s = tkinter.Label(calculatrice, text = "/",  font=("MADEAvenuePERSONALUSE-Regular",15))
        s.place(relx = 0.47, rely = 0.710, anchor = "center")
        n2 = tkinter.Label(calculatrice, text = str(tab[2]),  font=("MADEAvenuePERSONALUSE-Regular",15))
        n2.place(relx = 0.52, rely = 0.710, anchor = "center")

        eg = tkinter.Label(calculatrice, text = "=",  font=("MADEAvenuePERSONALUSE-Regular",15))
        eg.place(relx = 0.55, rely = 0.710, anchor = "center")
        
        resu = tkinter.Label(calculatrice, text = str(resi),  font=("MADEAvenuePERSONALUSE-Regular",15))
        resu.place(relx = 0.60, rely = 0.710, anchor = "center")
    else:
        resi = str("Error")
        resu = tkinter.Label(calculatrice, text = str(resi),  font=("MADEAvenuePERSONALUSE-Regular",15))
        resu.place(relx = 0.50, rely = 0.710, anchor = "center")

    tab.clear()

#Widgets
"""Création de menu"""
menu_calculatrice = tkinter.Menu(calculatrice)

AboutMenu = tkinter.Menubutton(calculatrice)

menu_calculatrice.add_cascade(label="About", menu=AboutMenu, command=fonction_calculatrice.description)

"""Création label,bouton et entry"""
texte1 = tkinter.Label(calculatrice, text="Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\nEnter choice(1/2/3/4):", font=("MADEAvenuePERSONALUSE-Regular",15))
texte1.place(relx=0.4999, rely=0.114, anchor= "center")


numero = tkinter.IntVar()
entree1 = tkinter.Entry(calculatrice,width=23,textvariable=numero,font=15)


entree1.place(relx = 0.50, rely = 0.255, anchor = "center")

texte2 = tkinter.Label(calculatrice, text="Select first number:", font=("MADEAvenuePERSONALUSE-Regular",15))
texte2.place(relx=0.4999, rely=0.365, anchor= "center")

numero1 = tkinter.IntVar()
entree2 = tkinter.Entry(calculatrice,width=23,textvariable=numero1,font=15)

entree2.place(relx = 0.50, rely = 0.403, anchor = "center")

texte3 = tkinter.Label(calculatrice, text="Select second number:", font=("MADEAvenuePERSONALUSE-Regular",15))
texte3.place(relx=0.4999, rely=0.513, anchor= "center")

numero2 = tkinter.IntVar()
entree3 = tkinter.Entry(calculatrice,width=23,textvariable=numero2,font=15)

entree3.place(relx = 0.50, rely = 0.553, anchor = "center")

bouton3 = tkinter.Button(calculatrice, text = "Calculation", font = ("MADEAvenuePERSONALUSE-Regular", 13), fg = "black", bg = "azure", command=res)
bouton3.place(relx = 0.50, rely = 0.610, anchor = "center")


#Boucle principale
calculatrice.config(menu=menu_calculatrice)
calculatrice.mainloop()