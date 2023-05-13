import canvas
import model

label_dict = {
    0: "geminae triangula",
    1: "spiralis",
    # adicione mais classes aqui
}


while True:
    cv = canvas.createCanvas()
    img = canvas.saveImage("predict.png")
    net = model.loadModel("./model.pth")
    print(label_dict[model.predict(net,img)])
    