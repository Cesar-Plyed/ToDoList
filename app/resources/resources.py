TITLE_FONT = ("Arial", 20)
TEXT_FONT = ("Arial", 15)

def get_height(w):
    w.update_idletasks()
    alto = w.winfo_height()
    return alto
    
def get_width(w):
    w.update_idletasks()
    ancho = w.winfo_width()
    return ancho

ICON = "C:\\Users\\cesar\\Documents\\Python-Projects\\Lavanderia\\views\\images\\Ico.ico"
LOGO = "C:\\Users\\cesar\\Documents\\Python-Projects\\Lavanderia\\views\\images\\Logo.jpg"

#Tercera paleta de colores
LABEL_COLOR = "#374151"
LABEL_TABLE_COLOR=  "#000000"    
TITLE_COLOR = "#06215C"             
BACKGROUND_COLOR = "#F3F4F6"        
BACKGROUND_BUTTON_COLOR = "#2563EB" 
BUTTON_TEXT_COLOR = "#ffffff"
BACKGROUND_TABLE_COLOR = "#FFFFFF"
BACKGROUND_DELETE_BUTTON = "#A50000"
BACKGROUND_EDIT_BUTTON = "#008B00"
BACKGROUND_HEADER_TABLE_COLOR = "#000000"