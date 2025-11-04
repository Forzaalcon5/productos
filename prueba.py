from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

raiz = Tk()
raiz.title("Tiendita de Comidas")
raiz.geometry("400x350")

carrito = []  # Lista de productos agregados

# FUNCIONES 

def abrir(imagen, nombre, precio):
    nueva = Toplevel(raiz)
    nueva.title("Producto seleccionado")
    nueva.geometry("300x350")

    Label(nueva, text=f"{nombre} - ${precio}", font=("Arial", 12)).pack(pady=10)

    nueva.imagen_mostrada = imagen
    Label(nueva, image=nueva.imagen_mostrada).pack(pady=10)

    cantidad = IntVar(value=1)

    def aumentar():
        cantidad.set(cantidad.get() + 1)

    def disminuir():
        if cantidad.get() > 1:
            cantidad.set(cantidad.get() - 1)

    frame_cantidad = Frame(nueva)
    frame_cantidad.pack(pady=10)

    Button(frame_cantidad, text="-", width=3, command=disminuir).grid(row=0, column=0)
    Label(frame_cantidad, textvariable=cantidad, font=("Arial", 14)).grid(row=0, column=1, padx=10)
    Button(frame_cantidad, text="+", width=3, command=aumentar).grid(row=0, column=2)

    def agregar_carrito():
        carrito.append({
            "producto": nombre,
            "precio": precio,
            "cantidad": cantidad.get()
        })
        nueva.destroy()  # Cerrar ventana al agregar

    Button(nueva, text="Agregar al carrito ", command=agregar_carrito).pack(pady=10)
    Button(nueva, text="Cancelar", command=nueva.destroy).pack(pady=5)


def actualizar_carrito():
    """Refrescar el contenido del carrito en la pestaña."""
    for widget in tab2.winfo_children():
        widget.destroy()

    Label(tab2, text=" Carrito de Compras", font=("Arial", 14, "bold")).pack(pady=10)

    if len(carrito) == 0:
        Label(tab2, text="No hay productos agregados").pack()
        return

    total = 0
    for item in carrito:
        subtotal = item['precio'] * item['cantidad']
        total += subtotal
        Label(tab2, text=f"{item['producto']} x {item['cantidad']} = ${subtotal}").pack(anchor="w", padx=20)

    Label(tab2, text=f"\nTotal: ${total}", font=("Arial", 12, "bold")).pack(pady=10)

    # Boton para ir a la pestaña de factura
    Button(tab2, text="Ver factura", font=("Arial", 11, "bold"), command=mostrar_factura).pack(pady=5)


def mostrar_carrito():
    """Cambia a la pestaña del carrito y actualiza el contenido."""
    actualizar_carrito()
    notebook.select(tab2)


def mostrar_factura():
    """Muestra los productos con detalle y total final."""
    for widget in tab3.winfo_children():
        widget.destroy()

    Label(tab3, text=" Factura de Compra", font=("Arial", 14, "bold")).pack(pady=10)

    if len(carrito) == 0:
        Label(tab3, text="No hay productos en el carrito").pack()
        return

    total_general = 0
    for item in carrito:
        subtotal = item['precio'] * item['cantidad']
        total_general += subtotal
        Label(tab3, text=f"{item['producto']}  x{item['cantidad']}  -  ${item['precio']} c/u  =  ${subtotal}").pack(anchor="w", padx=20)

    Label(tab3, text=f"\nTOTAL: ${total_general}", font=("Arial", 12, "bold"), fg="green").pack(pady=10)

#INTERFZA

notebook = ttk.Notebook(raiz)
notebook.pack(expand=True, fill='both')

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Menu")
notebook.add(tab2, text="Carrito")
notebook.add(tab3, text="Factura")

# Cargar imagenes
img1 = Image.open("awita.png").resize((80, 80))
img2 = Image.open("salchipapa.png").resize((80, 80))
img3 = Image.open("mojarra frita.png").resize((80, 80))

imagen1 = ImageTk.PhotoImage(img1)
imagen2 = ImageTk.PhotoImage(img2)
imagen3 = ImageTk.PhotoImage(img3)

#  Productos
productos = [
    ("Awita de coco", 20000, 20, imagen1),
    ("Salchipapa", 12000, 120, imagen2),
    ("Mojarra", 15000, 220, imagen3)
]

#  Mostrar productos
for (nombre, precio, y, image) in productos:
    lbl = Label(tab1, image=image, cursor="hand2")
    lbl.place(x=150, y=y)
    lbl.bind("<Button-1>", lambda e, i=image, n=nombre, p=precio: abrir(i, n, p))

# Boton para abrir el carrito
Button(tab1, text="Confirmar compra", font=("Arial", 12), command=mostrar_carrito).place(x=120, y=300)

raiz.mainloop()
