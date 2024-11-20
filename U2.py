# Librerias 
import tkinter, os, sys 
from tkinter import filedialog, messagebox, IntVar, PhotoImage, Menu
from tkinter.font import Font 
import webbrowser , re 
from pytube import YouTube

# Funciones de porgrmacion 

def obtener_ruta_absoluta (nombre_archivo): 
    carpeta_recursos = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join (carpeta_recursos, "recursos", nombre_archivo) 

def cargar_imagen(ruta): 
    imagen = PhotoImage(file=ruta)
    return imagen 

def mostrar_creditos(): 
    mensaje = "Autor: ArturoCid\n" \
              "YouTube: Cuyox3\n" \
              "SitioWeb: cuyox3.com\n"  \
              
    messagebox.showinfo("Creditos:", mensaje)

def descargar_video(url, ruta_video): 
    try:
        yt = YouTube(url) 
        video = yt.streams.get_highest_resolution()
        nombre_archivo = f"{yt.title}_vcuyox3.{video.mime_type.split('/')[-1]}"
        video.download(output_path = ruta_video,filename=nombre_archivo)

    except Exception:
        tkinter.messagebox.showwarning(tittle="Error", message="Error al descargar el video")

def descargar_audio(url, ruta_audio): 
    try:
        yt = YouTube(url) 
        audio = yt.streams.filter(only_audio=True).first()
        nombre_archivo = f"{yt.title}_acuyox3.{audio.mime_type.split('/')[-1]}"
        audio.download(output_path = ruta_audio, filename = nombre_archivo)

    except Exception:
        tkinter.messagebox.showwarning(tittle="Error", message="Error al descargar el auido")

def validar_url(url):
    youtube_valida = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be\/.+$)"
    return re.match(youtube_valida,url)

def ejecutar():
    url = entry_url.get()
    #limpiar 
    resultado.config(text="",bg="white")
    entry_url.delete(0,tkinter.END)
    if validar_url(url):
        if opc.get() == 1:
            ruta_guardado = filedialog.askdirectory()
            descargar_video(url, ruta_guardado)
            entry_ruta.insert(0,ruta_guardado)
            tkinter.messagebox.showinfo(title="Hecho",message="Video descargado correctamente !")
        elif opc.get() == 2:
            ruta_guardado = filedialog.askdirectory()
            descargar_audio(url, ruta_guardado)
            entry_ruta.insert(0,ruta_guardado)
            tkinter.messagebox.showinfo(title="Hecho",message="Audio descargado correctamente !")
        else:
            tkinter.messagebox.showwarning(title="Advertecia", message="Tienes que seleccionar si quieres descargar audio o video")
    else:
        resultado.config(text="Url no valida",fg= "red",bg="white")
        entry_url.delete(0,tkinter.END)
# Ventana
ventana = tkinter.Tk() 
ventana.title("Pytube by:Cuyox3 BETA")
ventana.config(bg="white")
ancho= 800 
alto = 610
ancho_pantalla = ventana .winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
alinear = '%dx%d+%d+%d' % (ancho, alto,(ancho_pantalla - ancho) /2,(alto_pantalla - alto)/2 )
ventana.geometry(alinear)
ventana.resizable(width=False, height=False) 
icono = tkinter.PhotoImage(file=obtener_ruta_absoluta("icono.png"))
icono_b = tkinter.PhotoImage(file=obtener_ruta_absoluta("icono_b.png"))
ventana.iconphoto(False, icono_b, icono) 
# Menu
## Creacion de barra de menu
barra_menu = tkinter.Menu(ventana)
ventana.config(menu=barra_menu)
## Creacion de opciones de cascada del menu 
menu_archivo = tkinter.Menu(ventana,tearoff=False)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_cascade(label="Configurar")
menu_archivo.add_command(label="Salir",compound=tkinter.LEFT,command=ventana.destroy)

menu_ayuda = tkinter.Menu(ventana,tearoff=False)
barra_menu.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Creditos",command=mostrar_creditos)
# Variables 
frame= tkinter.Frame(ventana, bg="black")
frame.pack()
fuente = tkinter.font.Font(family="Roboto Cn",size=11)
fuente_b = tkinter.font.Font(family="Roboto Cn",size=14)
imagen = cargar_imagen(obtener_ruta_absoluta("logo-dt.png"))
# Imagen
label_imagen = tkinter.Label(frame, image=imagen, bg="black" )
label_imagen.grid(row=0,column=0,padx=60, pady=20)
# Inicio de ventanas que se utilizan 
labelFrame_youtube = tkinter.LabelFrame(frame,text = "Informacion de Youtube",bg="white",font=fuente)
labelFrame_youtube.grid(row=1, column=0, padx=20, pady=10)
# URL
label_url = tkinter.Label(labelFrame_youtube,text="Introduce el URL",bg="white",font=fuente)
label_url.grid(row=0, column=0)
entry_url = tkinter.Entry(labelFrame_youtube, width=40,border=5,font=fuente)
entry_url.grid(row=0,column=1, padx=20, pady= 10)
#resultado de verificacion 
resultado = tkinter.Label(labelFrame_youtube,text="",fg="white")
resultado.grid(row=3, columnspan=3 ) 
# Ruta
label_ruta = tkinter.Label(labelFrame_youtube,text="Introduce la ruta",bg="white",font=fuente)
label_ruta.grid(row=1, column=0)
entry_ruta = tkinter.Entry(labelFrame_youtube, width=40,border=5, font=fuente)
entry_ruta.grid(row=1,column=1, padx=20, pady= 10)
# Opciones 
labelFrame_tipo = tkinter.LabelFrame(frame,text="Tipo de descarga",bg="white",font=fuente)
labelFrame_tipo.grid(row=2, column=0, padx=20, pady= 10)
opc = IntVar()
recuerda = tkinter.Label(labelFrame_tipo, text="**El video tarda, no cierres el programa cx", bg="white",font=fuente)
recuerda.grid(row=0, column=3, padx=20, pady= 10)
video = tkinter.Radiobutton(labelFrame_tipo, text="Video", value=1, bg="white",font=fuente, variable=opc)
video.grid(row=0, column=0, padx=20, pady= 10)
audio = tkinter.Radiobutton(labelFrame_tipo,text="Audio", value=2, bg="white", font=fuente, variable=opc)
audio.grid(row=0, column=1, padx=20, pady= 10)
# Boton 
button = tkinter.Button(frame, text="Descargar !", font=fuente_b,bg="red", fg="white", command=ejecutar)
button.grid (row=3,column=0, padx=20,pady=10,sticky="news")
#Inicio de ventana
ventana.mainloop()
