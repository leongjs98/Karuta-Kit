import pyautogui    # Auto-typing
import keyboard     # Detect if "ESC" is hit
import time         # Time interval between each entry
import re

# For the simple user interface
import tkinter as tk
from tkinter import messagebox

pointer_position = [0, 0]
BG_COLOR = '#2f3136'
FG_COLOR = '#b9bbbe'
WIDGET_COLOR = '#3a4c48'
INST_FONT_SIZE = 13
CHECKBOX_FONT_SIZE = 11


def main():
    root = tk.Tk()
    root.title('Card Hunting')
    root.configure(bg=BG_COLOR)
    root.resizable(width=False, height=False)

    #----------------------------Detection starts----------------------------
    frame_detect = tk.LabelFrame(root, text="Where to type?", padx=10, pady=10, bg=BG_COLOR, fg=FG_COLOR, bd=1)
    frame_detect.pack(padx=10, pady=10)

    # Instruction
    inst_detect = tk.Label(frame_detect, text='Press "Ctrl" after clicking  ')
    inst_detect.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_detect.grid(row=2, column=1)

    def detect_pointer():
        keyboard.wait('ctrl')
        pointer_position[0] = pyautogui.position()[0]
        pointer_position[1] = pyautogui.position()[1]

        if pointer_position[0] and pointer_position[1]:
            click_txt.set(f'Position detected: {pointer_position[0]}, {pointer_position[1]}')
        
    # Left click on where the user wants to type in
    click_txt = tk.StringVar()
    click_btn = tk.Button(frame_detect, command=detect_pointer, textvariable=click_txt, height=1, width=25)
    click_btn.config(font=('Arial', INST_FONT_SIZE), fg=FG_COLOR, bg=WIDGET_COLOR)
    click_btn.grid(row=2, column=2, pady=INST_FONT_SIZE)
    click_txt.set('Detect')
    #----------------------------Detection ends----------------------------

    #----------------------------Card name starts----------------------------
    frame_name = tk.LabelFrame(root, padx=10, pady=10, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_name.pack(padx=10, pady=10)

    inst_name = tk.Label(frame_name, text='Card name:  ')
    inst_name.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_name.grid(row=1, column=0)

    card_name = tk.StringVar()
    card_name_entry = tk.Entry(frame_name, textvariable=card_name, borderwidth=3, width=50)
    card_name_entry.grid(row=1, column=1)
    #----------------------------Card name ends----------------------------

    #----------------------------Card codes starts----------------------------
    frame_codes = tk.LabelFrame(root, padx=10, pady=10, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_codes.pack(padx=10, pady=10)

    inst_code = tk.Label(frame_codes, text='Card codes:  ')
    inst_code.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_code.grid(row=1, column=0)

    card_code = tk.StringVar()
    card_code_entry = tk.Entry(frame_codes, textvariable=card_code, borderwidth=3, width=50)
    card_code_entry.grid(row=1, column=1)
    #----------------------------Card codes ends----------------------------

    #----------------------------Condition checkboxes starts----------------------------
    frame_checkboxes = tk.LabelFrame(root, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_checkboxes.pack(padx=10, pady=10)

    var_damaged = tk.IntVar()
    var_poor = tk.IntVar()
    var_good = tk.IntVar()
    var_excellent = tk.IntVar()
    var_mint = tk.IntVar()

    inst_code = tk.Label(frame_checkboxes, text='Conditions:  ')
    inst_code.config(font=('Helvetica', CHECKBOX_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_code.grid(row=0, column=0)

    damaged_checkbox = tk.Checkbutton(frame_checkboxes, text="Damaged", variable=var_damaged, onvalue=1, offvalue=0)
    damaged_checkbox.config(font=('Helvetica', CHECKBOX_FONT_SIZE))
    damaged_checkbox.grid(row=0, column=1)

    poor_checkbox = tk.Checkbutton(frame_checkboxes, text="Poor", variable=var_poor, onvalue=1, offvalue=0)
    poor_checkbox.config(font=('Helvetica', CHECKBOX_FONT_SIZE))
    poor_checkbox.grid(row=0, column=2)

    good_checkbox = tk.Checkbutton(frame_checkboxes, text="Good", variable=var_good, onvalue=1, offvalue=0)
    good_checkbox.config(font=('Helvetica', CHECKBOX_FONT_SIZE))
    good_checkbox.grid(row=0, column=3)

    excellent_checkbox = tk.Checkbutton(frame_checkboxes, text="Excellent", variable=var_excellent, onvalue=1, offvalue=0)
    excellent_checkbox.config(font=('Helvetica', CHECKBOX_FONT_SIZE))
    excellent_checkbox.grid(row=0, column=4)

    mint_checkbox = tk.Checkbutton(frame_checkboxes, text="Mint", variable=var_mint, onvalue=1, offvalue=0)
    mint_checkbox.config(font=('Helvetica', CHECKBOX_FONT_SIZE))
    mint_checkbox.grid(row=0, column=5)
    #----------------------------Condition checkboxes ends----------------------------

    #----------------------------Typing interval starts----------------------------
    frame_interval = tk.LabelFrame(root, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_interval.pack(padx=10, pady=10)

    inst_interval = tk.Label(frame_interval, text='Interval (seconds):  ')
    inst_interval.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_interval.grid(row=0, column=0)
    
    def autotype():

        # Get the desired conditions
        condition_list = []
        if var_damaged.get() == 1:
            condition_list.append("damaged")
        else:
            if "damaged" in condition_list:
                condition_list.remove("damaged")

        if var_poor.get() == 1:
            condition_list.append("poor")
        else:
            if "poor" in condition_list:
                condition_list.remove("poor")

        if var_good.get() == 1:
            condition_list.append("good")
        else:
            if "good" in condition_list:
                condition_list.remove("good")

        if var_excellent.get() == 1:
            condition_list.append("excellent")
        else:
            if "excellent" in condition_list:
                condition_list.remove("excellent")

        if var_mint.get() == 1:
            condition_list.append("mint")
        else:
            if "mint" in condition_list:
                condition_list.remove("mint")

        # Find out the wanted card codes and their conditions
        card_name = card_name_entry.get().strip()  # Get the name and remove the empty spaces at both ends
        cards = card_code_entry.get()
        unformat_cards = re.findall(r"took the " + card_name + r".+", cards)
        
        card_list = []
        for card in unformat_cards:
            unformat_code = re.search("\w{6,}!", card).group()
            code = re.sub("!", "", unformat_code)

            unformat_condition = re.search("\w{4,9} condition", card)
            if unformat_condition:
                condition = re.sub(" condition", "", unformat_condition.group())
            else:
                condition = "poor"
            card_dict = {"code": code, "condition": condition}
            card_list.append(card_dict)

        # Start typing
        command = ""
        i = 0
        for card in card_list:
            # command = "kci"
            if card["condition"] in condition_list:
                if card:
                    if i % 3 == 1:
                        command = "kv"
                    elif i % 3 == 2:
                        command = "kci"
                    elif i % 3 == 0:
                        command = "kwi"

                    if keyboard.is_pressed("esc"):
                        break
                    
                    pyautogui.click(pointer_position[0], pointer_position[1])
                    pyautogui.write(f'{command} {card["code"]}')
                    pyautogui.press('enter')
                    time.sleep(int(interval_entry.get()))

                    i += 1
        
        stop_typing()
        
    # Time interval between typing
    drop_txt = tk.StringVar()
    drop_txt.set('3')
    interval_entry = tk.ttk.Entry(root, textvariable=drop_txt)
    
    drop = tk.OptionMenu(frame_interval, drop_txt, '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')
    drop.config(font=('Arial', INST_FONT_SIZE), fg=FG_COLOR, bg=WIDGET_COLOR)
    drop.grid(row=0, column=1)
    #----------------------------Typing interval ends----------------------------

    #----------------------------Start and Exit Button starts----------------------------
    frame_btn = tk.LabelFrame(root, padx=10, pady=10, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_btn.pack(padx=10)

    # Start button
    start_btn = tk.Button(frame_btn, command=autotype, text='Start', height=1, width=7)
    start_btn.config(font=('Arial', INST_FONT_SIZE), fg=FG_COLOR, bg=WIDGET_COLOR)
    start_btn.grid(row=0, column=0, padx=20)


    # Exit button
    exit_btn = tk.Button(frame_btn, command=root.quit, text='Exit', height=1, width=7)
    exit_btn.config(font=('Arial', INST_FONT_SIZE), fg=FG_COLOR, bg=WIDGET_COLOR)
    exit_btn.grid(row=0, column=1)


    frame_inst = tk.LabelFrame(root, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_inst.pack()
    inst_stop = tk.Label(frame_inst, text='Hold "esc" to stop.')
    inst_stop.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_stop.grid(row=0, column=0, pady=10)
    #----------------------------Start and Exit Button ends----------------------------


    root.mainloop()


def stop_typing():
    tk.messagebox.showinfo('Card Hunting', 'Typing stopped.')


main()