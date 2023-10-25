from customtkinter import *
from function import *
from PIL import Image

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


def innit_cezar_decode():
    try:
        decoded_text = cezar_decode(txt_input.get(0.1, "end"), int(txt_key_write.get()))
    except ValueError:
        print("ошибка")

    try:
        txt_output.delete(0.1, "end")
        txt_output.insert(0.1, decoded_text)
    except UnboundLocalError:
        pass


def innit_vizhener_enocode():
    try:
        enocoded_text2 = vizhener_enocode(txt_input_2.get(0.1, "end"), (txt_key_w2.get()))
    except ValueError:
        print("ошибка")

    try:
        txt_output_2.delete(0.1, "end")
        txt_output_2.insert(0.1, enocoded_text2)
    except UnboundLocalError:
        pass


def innit_vizhener_decode():
    try:
        decoded_text2 = vizhener_decode(txt_input_2.get(0.1, "end"), (txt_key_w2.get()))
    except ValueError:
        print("ошибка")

    try:
        txt_output_2.delete(0.1, "end")
        txt_output_2.insert(0.1, decoded_text2)
    except UnboundLocalError:
        pass


def innit_hex_enocode():
    try:
        enocoded_text3 = hex_enocode(txt_input_3.get(0.1, "end"))
    except ValueError:
        print("ошибка")

    try:
        txt_output_3.delete(0.1, "end")
        txt_output_3.insert(0.1, enocoded_text3)
    except UnboundLocalError:
        pass


def innit_hex_decode():
    try:
        decoded_text3 = hex_decode(txt_input_3.get(0.1, "end"))
    except ValueError:
        print("ошибка")

    try:
        txt_output_3.delete(0.1, "end")
        txt_output_3.insert(0.1, decoded_text3)
    except UnboundLocalError:
        pass


def innit_atbash_cipher():
    try:
        enocoded_text4 = atbash_cipher(txt_input_4.get(0.1, "end"))
    except ValueError:
        print("ошибка")

    try:
        txt_output_4.delete(0.1, "end")
        txt_output_4.insert(0.1, enocoded_text4)
    except UnboundLocalError:
        pass


def innit_atbash_decipher():
    try:
        decoded_text4 = atbash_decipher(txt_input_4.get(0.1, "end"))
    except ValueError:
        print("ошибка")

    try:
        txt_output_4.delete(0.1, "end")
        txt_output_4.insert(0.1, decoded_text4)
    except UnboundLocalError:
        pass


def innit_copyresault():
    copyresault(txt_output.get(0.1, "end"))


def innit_pastecopyed():
    result = pastecopyed()
    txt_input.delete(0.1, "end")
    txt_input.insert("end", result)




def innit_copyresault_2():
    copyresault(txt_output_2.get(0.1, "end"))


def innit_pastecopyed_2():
    result = pastecopyed()
    txt_input_2.delete(0.1, "end")
    txt_input_2.insert("end", result)




def innit_copyresault_3():
    copyresault(txt_output_3.get(0.1, "end"))


def innit_pastecopyed_3():
    result = pastecopyed()
    txt_input_3.delete(0.1, "end")
    txt_input_3.insert("end", result)




def innit_copyresault_4():
    copyresault(txt_output_4.get(0.1, "end"))


def innit_pastecopyed_4():
    result = pastecopyed()
    txt_input_4.delete(0.1, "end")
    txt_input_4.insert("end", result)




#создание окна
window = CTk()
window.title("𝕾𝖍𝖎𝖋𝖗𝖆𝖙𝖔𝖗")
window.geometry("750x500+600+250")
window.resizable(False, False)

pathIco = "Images/иконка.ico"
window.iconbitmap(pathIco)

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

bgimage = CTkImage(Image.open('Images/VK.png'), size = (750, 500))
imagelabel = CTkLabel(window, image = bgimage, text =' ')
imagelabel.place(x = 0, y = 0)

copyright_1 = CTkLabel(window, text = "Сакичева Аксинья, 2023г")
copyright_1.place(x = 593, y = 468)

#выбор вкладки(шифра)
tabview = CTkTabview(window, width=650, height=380)
tabview.place(x = 50, y = 58)
tabview.add("шифр цезаря")
tabview.add("шифр виженера")
tabview.add("HEX-кодирование")
tabview.add("Атбаш")
tabview.set("шифр цезаря")

#текст в окне шифр цезаря
txt_input =CTkTextbox(tabview.tab("шифр цезаря"), width = 240, height = 230)
txt_input.place(x = 40, y = 20)
txt_output = CTkTextbox(tabview.tab("шифр цезаря"), width = 240, height = 230)
txt_output.place(x = 360, y= 20)
txt_key_write = CTkEntry(tabview.tab("шифр цезаря"), width = 100)
txt_key_write.place(x = 270, y = 289)
text_key = CTkLabel(tabview.tab("шифр цезаря"), text = "ключ")
text_key.place(x = 304, y = 259)

#текст в окне шифр виженера
txt_input_2 = CTkTextbox(tabview.tab("шифр виженера"), width = 240, height = 230)
txt_input_2.place(x = 40, y = 20)
txt_output_2 = CTkTextbox(tabview.tab("шифр виженера"), width = 240, height = 230)
txt_output_2.place(x = 360, y = 20)
txt_key_w2 = CTkEntry(tabview.tab("шифр виженера"), width = 100)
txt_key_w2.place(x = 270, y = 289)
text_key_2 = CTkLabel(tabview.tab("шифр виженера"), text = "ключ")
text_key_2.place(x = 304, y = 259)

#текст в окне HEX-кодирование
txt_input_3 = CTkTextbox(tabview.tab("HEX-кодирование"), width = 240, height = 230)
txt_input_3.place(x = 40, y = 20)
txt_output_3 = CTkTextbox(tabview.tab("HEX-кодирование"), width = 240, height = 230)
txt_output_3.place(x = 360, y = 20)

#текст в окне Атбаш
txt_input_4 = CTkTextbox(tabview.tab("Атбаш"), width = 240, height = 230)
txt_input_4.place(x = 40, y = 20)
txt_output_4 = CTkTextbox(tabview.tab("Атбаш"), width = 240, height = 230)
txt_output_4.place(x = 360, y = 20)

#кнопки цезаря
btn_enocode = CTkButton(tabview.tab("шифр цезаря"), text = "Зашифровать", command = innit_cezar_enocode)
btn_enocode.place(x = 88, y = 260)
btn_decode =CTkButton(tabview.tab("шифр цезаря"), text = "Расшифровать", command = innit_cezar_decode)
btn_decode.place(x= 412, y = 260)

#кнопки виженера
btn_enocode_2 = CTkButton(tabview.tab("шифр виженера"), text = "Зашифровать", command = innit_vizhener_enocode)
btn_enocode_2.place(x = 88, y = 260)
btn_decode_2 =CTkButton(tabview.tab("шифр виженера"), text = "Расшифровать", command = innit_vizhener_decode)
btn_decode_2.place(x= 412, y = 260)

#кнопки HEX-кодирования
btn_enocode_3 = CTkButton(tabview.tab("HEX-кодирование"), text = "Зашифровать", command = innit_hex_enocode)
btn_enocode_3.place(x = 88, y = 260)
btn_decode_3 =CTkButton(tabview.tab("HEX-кодирование"), text = "Расшифровать", command = innit_hex_decode)
btn_decode_3.place(x= 412, y = 260)

#кнопки Атбаш
btn_enocode_4 = CTkButton(tabview.tab("Атбаш"), text = "Зашифровать", command = innit_atbash_cipher)
btn_enocode_4.place(x = 88, y = 260)
btn_decode_4 =CTkButton(tabview.tab("Атбаш"), text = "Расшифровать", command = innit_atbash_decipher)
btn_decode_4.place(x= 412, y = 260)

#кнопки копирование-вставка
btn_copy_1 = CTkButton(tabview.tab("шифр цезаря"), text = "Сopy", width = 45, height = 35, command = innit_copyresault)
btn_copy_1.place(x = 298, y = 90)
btn_paste_1 = CTkButton(tabview.tab("шифр цезаря"), text = "Paste", width = 45, height = 35, command = innit_pastecopyed)
btn_paste_1.place(x = 298, y = 150)

btn_copy_2 = CTkButton(tabview.tab("шифр виженера"), text = "Сopy", width = 45, height = 35, command = innit_copyresault_2)
btn_copy_2.place(x = 298, y = 90)
btn_paste_2 = CTkButton(tabview.tab("шифр виженера"), text = "Paste", width = 45, height = 35, command = innit_pastecopyed_2)
btn_paste_2.place(x = 298, y = 150)

btn_copy_3 = CTkButton(tabview.tab("HEX-кодирование"), text = "Сopy", width = 45, height = 35, command = innit_copyresault_3)
btn_copy_3.place(x = 298, y = 90)
btn_paste_3 = CTkButton(tabview.tab("HEX-кодирование"), text = "Paste", width = 45, height = 35, command = innit_pastecopyed_3)
btn_paste_3.place(x = 298, y = 150)

btn_copy_3 = CTkButton(tabview.tab("Атбаш"), text = "Сopy", width = 45, height = 35, command = innit_copyresault_4)
btn_copy_3.place(x = 298, y = 90)
btn_paste_3 = CTkButton(tabview.tab("Атбаш"), text = "Paste", width = 45, height = 35, command = innit_pastecopyed_4)
btn_paste_3.place(x = 298, y = 150)


window.mainloop()