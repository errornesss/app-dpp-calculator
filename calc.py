import tkinter as tk

main = tk.Tk()
main.title('APP/DPP calculator')
main.geometry('360x480')

# functions --
def calculation(stat):
    pps = float(pps_input.get())
    apm = float(apm_input.get())
    vs = float(vs_input.get())
    app = apm/pps/60
    dpp = ((3*vs-5*apm)/(300*pps))
    if stat == 'app':
        return app
    elif stat == 'dpp':
        return dpp

def calculation_display():
    display_app = calculation('app')
    display_dpp = calculation('dpp')

    calculation_box = tk.Text(master=main, width=15, height=10)
    calculation_box.grid(row=5, column=0)

    calculation_box.insert(tk.END, f'PPS: {pps_input.get()} \nAPM: {apm_input.get()} \nVS: {vs_input.get()} \n\nAPP: {round(display_app, 4)} \nDPP: {round(display_dpp, 4)}')

# title --
title = tk.Label(text='Calculator')
title.grid(row=0, column=0)

# inputs --
pps_title = tk.Label(text='PPS:')
pps_title.grid(row=1, column=0)
pps_input = tk.Entry()
pps_input.grid(row=1, column=1)

apm_title = tk.Label(text='APM:')
apm_title.grid(row=2, column=0)
apm_input = tk.Entry()
apm_input.grid(row=2, column=1)

vs_title = tk.Label(text='VS:')
vs_title.grid(row=3, column=0)
vs_input = tk.Entry()
vs_input.grid(row=3, column=1)

#button --
calculate = tk.Button(text='Calculate', command=calculation_display)
calculate.grid(row=4, column=0)

main.mainloop()