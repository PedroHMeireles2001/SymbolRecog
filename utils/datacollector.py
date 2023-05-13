import canvas



i = 0
while True:
    i += 1
    canvas.createCanvas()
    img = canvas.toImage()
    img.save(r"C:\Users\pedro\OneDrive\Imagens\SymbolDataset\Symbol3\canvas"+str(i)+".png", "png")