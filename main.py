from customtkinter import *
from function import *

def innit_cezar_enocode():
    try:
        enocoded_text = cezar_enocode(txt_input.get(0.1, "end"), int(txt_key_write.get()))
    except ValueError:
        print("ошибка")

    try:
        txt_output.delete(0.1, "end")
        txt_output.insert(0.1, enocoded_text)
    except UnboundLocalError:
        pass

#создание окна
window = CTk()
window. title ("Шифратор")
window.geometry("750x500+600+250")
window.resizable(False, False)

set_appearance_mode('dark')
set_default_color_theme('dark-blue')


#текст в окне
txt_input =CTkTextbox(window, width = 250, height = 250)
txt_input.place(x = 100, y = 60)
txt_output = CTkTextbox(window, width = 250, height = 250)
txt_output.place(x = 400, y= 60)
txt_key_write = CTkEntry(window, width = 100)
txt_key_write.place(x = 323, y = 400)
text_key = CTkLabel(window, text = "ключ")
text_key.place(x = 356, y = 369)
#кнопка
btn_enocode = CTkButton(window, text = "Зашифровать", command = innit_cezar_enocode)
btn_enocode.place(x = 157, y = 320)
btn_decode =CTkButton(window, text = "Расшифровать")
btn_decode.place(x= 456, y = 320)

window .mainloop()