import pyautogui    # Auto-typing
import keyboard     # Detect if "ESC" is hit
import time         # Time interval between each entry

# For the simple user interface
import tkinter as tk


pointer_position = [0, 0]
BG_COLOR = '#2f3136'
FG_COLOR = '#b9bbbe'
WIDGET_COLOR = '#3a4c48'
INST_FONT_SIZE = 13


def main():
    root = tk.Tk()
    root.title('Dye Test')
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
    
    #----------------------------Card and Dye codes starts----------------------------
    frame_codes = tk.LabelFrame(root, padx=10, pady=10, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_codes.pack(padx=10, pady=10)

    # # Instruction
    inst_card = tk.Label(frame_codes, text='Card code:  ')
    inst_card.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_card.grid(row=0, column=0)

    card_code = tk.StringVar()
    card_entry = tk.Entry(frame_codes, textvariable=card_code, borderwidth=3, width=50)
    card_entry.grid(row=0, column=1)

    inst_dye = tk.Label(frame_codes, text='Dye code:  ')
    inst_dye.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_dye.grid(row=1, column=0)

    dye_code = tk.StringVar()
    dye_entry = tk.Entry(frame_codes, textvariable=dye_code, borderwidth=3, width=50)
    dye_entry.grid(row=1, column=1)
    #----------------------------Card and Dye codes ends----------------------------

    #----------------------------Typing interval starts----------------------------
    frame_interval = tk.LabelFrame(root, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_interval.pack(padx=10, pady=10)

    inst_interval = tk.Label(frame_interval, text='Interval (seconds):  ')
    inst_interval.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_interval.grid(row=0, column=0)
    
    def autotype_dye_test():
        dyes = dye_entry.get().split(" ")
        
        for dye in dyes:
            if dye:
                if keyboard.is_pressed("esc"):
                    break

                pyautogui.click(pointer_position[0], pointer_position[1])
                pyautogui.write(f'kdye {card_entry.get()} {dye}')
                pyautogui.press('enter')
                time.sleep(int(interval_entry.get()))
        
        stop_testing()
        
    # Time interval between typing
    drop_txt = tk.StringVar()
    drop_txt.set('2')
    interval_entry = tk.ttk.Entry(root, textvariable=drop_txt)
    
    drop = tk.OptionMenu(frame_interval, drop_txt, '1', '2', '3', '4', '5', '6', '7', '8')
    drop.config(font=('Arial', INST_FONT_SIZE), fg=FG_COLOR, bg=WIDGET_COLOR)
    drop.grid(row=0, column=1)
    #----------------------------Typing interval ends----------------------------

    #----------------------------Start and Exit Button starts----------------------------
    frame_btn = tk.LabelFrame(root, padx=10, pady=10, bg=BG_COLOR, fg=FG_COLOR, bd=0)
    frame_btn.pack(padx=10)

    # Start button
    start_btn = tk.Button(frame_btn, command=autotype_dye_test, text='Start', height=1, width=7)
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
    inst_stop.grid(row=0, column=0, pady=5)

    inst_readme = tk.Label(frame_inst, text='Check README.md for instructions')
    inst_readme.config(font=('Helvetica', INST_FONT_SIZE), fg=FG_COLOR, bg=BG_COLOR)
    inst_readme.grid(row=1, column=0, pady=5)
    #----------------------------Start and Exit Button ends----------------------------


    root.mainloop()


def stop_testing():
    tk.messagebox.showinfo('Dye Tester', 'Testing stopped.')


main()