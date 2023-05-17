from tkinter import *
from PIL import Image


HEIGHT = 400
WIDTH = 400


def createCanvas():

    root = Tk()
    root.title("Canvas")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.resizable(False , False)

    def paint(event):
        x = event.x
        y = event.y
        canvas.create_oval(x,y,x+20,y+20,fill="black")
        canvas.postscript(file="tmp_canvas.eps",
                  colormode="color",
                  width=WIDTH,
                  height=HEIGHT,
                  pagewidth=WIDTH-1,
                  pageheight=HEIGHT-1)
    def closeCanvas(event):
        root.destroy()
        
    
    

    canvas = Canvas(root , height=HEIGHT , width=WIDTH , bg="white")
    canvas.grid(row=0 , column=0)
    
    canvas.bind("<B1-Motion>",paint)
    canvas.bind("<ButtonRelease-1>",closeCanvas)
    
    
    root.mainloop()
    return canvas
def toImage():
    return Image.open("tmp_canvas.eps")
def saveImage(path):
    img = toImage()
    img.save(path,"png")
    return Image.open(path)

if __name__ == "__main__":
    createCanvas()