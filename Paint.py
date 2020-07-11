from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import PIL.ImageGrab as ImageGrab
from future.moves.tkinter import filedialog


class Paint_lite():
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("1366x768+1+1")
        self.root.configure(background='steel blue')
        # self.root.resizable(0, 0)

# Making Widget for the app

        # Colors
        self.penColor = "black"
        self.eraser_color = "white"

        self.color_frame = LabelFrame(self.root, text='Colors', font=(
            'consolas', 15), bd=5, relief=RIDGE, bg='white')
        self.color_frame.place(x=10, y=6, width=430, height=115)

        colors = ["#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF",
                  "#C0C0C0", "#808080", "#800000", "#808000", "#008000", "#800080", "#008080", "#000080"]
        i = j = 0
        for color in colors:
            Button(self.color_frame, bg=color, bd=2, relief=RIDGE,
                   width=6, height=2, command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
            j += 1
            if j == 8:
                j = 0
                i = 1

    # Create Color pen function

        # eraser Button
        self.eraser_button = Button(
            self.root, text="Eraser", bd=4, bg='white', command=self.eraser, width=7, relief=RIDGE)
        self.eraser_button.place(x=585, y=6, height=110)

        # Background Color
        self.eraser_button = Button(
            self.root, text="Backgound", bd=4, bg='white', command=self.bg_color, width=7, relief=RIDGE)
        self.eraser_button.place(x=455, y=36, height=50, width=100)

        #  scale Frame

        self.penScale_frame = LabelFrame(self.root, text='Scale', font=(
            'consolas', 12), bd=4, relief=RIDGE, bg='white')
        self.penScale_frame.place(x=680, y=28, width=270, height=70)

        self.penSize = Scale(self.penScale_frame,
                             orient=HORIZONTAL, from_=0, to=100, length=230, fg='blue')
        self.penSize.set(1)
        self.penSize.grid(row=0, column=1, padx=10)

        #  Clear Button

        self.clear_button = Button(
            self.root, text="Clear All", bd=4, bg='white', command=lambda: self.canvas.delete("all"), width=7, relief=RIDGE)
        self.clear_button.place(x=980, y=43, width=70)

        # Save Button

        self.save_button = Button(
            self.root, text="Save", bd=4, bg='white', command=self.save_p, width=7, relief=RIDGE)
        self.save_button.place(x=1080, y=43, width=70)

        # Exit Button

        self.save_button = Button(
            self.root, text="Exit", bd=4, bg='white', command=self.exit_p, width=7, relief=RIDGE)
        self.save_button.place(x=1180, y=43, width=70)

        # Canvas Frame

        self.canvas = Canvas(self.root, bg='white', bd=5,
                             relief=GROOVE, height=510, width=1305)
        self.canvas.place(x=21, y=140)

        # Copyright Footer
        self.label = Label(self.root, text="                                                            Copyright © Reserved to Saiyam Jain Corporations ",
                           font=('consolas', 12), bg='grey', relief=RIDGE)
        self.label.place(x=0, y=688, width=1366, height=25)

        # Binding mouse with application
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)

        self.canvas.create_oval(
            x1, y1, x2, y2, fill=self.penColor, outline=self.penColor, width=self.penSize.get())

    # Color Function

    def select_color(self, col):
        self.penColor = col

    # Eraser Function

    def eraser(self):
        self.penColor = self.eraser_color

    # Background Color Function

    def bg_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]

    # Save Function
    def save_p(self):
        try:
            # filename = filedialog.asksaveasfilename
            filename = filedialog.asksaveasfilename(defaultextension='.jpg')
            print(filename)
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            print(x, self.canvas.winfo_x())

            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            print(y, self.canvas.winfo_y())

            x1 = x + self.canvas.winfo_width()
            print(x1)

            y1 = y + self.canvas.winfo_height()
            print(y1)

            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
            messagebox.showinfo("Paint", "Image is saved as " + str(filename))

        except:
            messagebox.showerror(
                "Paint", "Something went wrong. Unable to save the image.")

    # EXIT FUNCTION

    def exit_p(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit")
        if op > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    P = Paint_lite(root)
    # root.iconbitmap('paint_icon.ico')
    root.mainloop()
