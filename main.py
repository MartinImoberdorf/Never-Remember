__author__ = 'Martín José Imoberdorf'

#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

import json
import datetime
import tkinter, tkinter.messagebox
import win32console
import win32gui

v=win32console.GetConsoleWindow()
win32gui.ShowWindow(v,0)

def messagebox(title, text):
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo(title, text)
    root.destroy()



def main():
    dia=datetime.datetime.now().strftime("%d")
    mes=datetime.datetime.now().strftime("%m")

    ruta='distribuidor.json'
    with open(ruta) as contenido:
        resultado=json.load(contenido)
        for i in resultado:
            if i.get('mes')==mes:
                ruta=i.get('nombre_archivo')

    with open(ruta) as contenido:
        resultado=json.load(contenido)
        for i in resultado:
            if i.get('dia')==dia:
                if i.get('mes')==mes:
                    messagebox("NR",i.get('nombre_evento'))


if __name__=='__main__':
    main()