import tkinter as Dima
x=0
y=50
win = Dima.Tk()
canvas = Dima.Canvas(win, bg='#0305B3', height = 400, width=400)
for a in range(0, 400, 100):
    canvas.create_oval((a, 0),(a+50, 50), fill = "#15C7FF")
for a in range(50, 400, 100):
    canvas.create_oval((a, 50),(a+50, 100), fill = "#15C7FF")
for a in range(0, 400, 100):
    canvas.create_oval((a, 100),(a+50, 150), fill = "#15C7FF")

for a in range(50, 400, 100):
    canvas.create_oval((a, 250),(a+50, 300), fill = "#12FF05")
for a in range(0, 400, 100):
    canvas.create_oval((a, 300),(a+50, 350), fill = "#12FF05")
for a in range(50, 400, 100):
    canvas.create_oval((a, 350),(a+50, 400), fill = "#12FF05")

for i in range(50, 400, 50):
    canvas.create_line((0, i), (500, i), fill="#0995A9")
    canvas.create_line((i, 0), (i, 500), fill="#0995A9")
canvas.pack()





canvas.pack()



Dima.mainloop()