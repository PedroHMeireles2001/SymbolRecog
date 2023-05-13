import canvas
import model

label_dict = {
    0: "geminae triangula",
    1: "spiralis"
    # adicione mais classes aqui
}

net = model.loadModel("./model.pth")
while True:
    cv = canvas.createCanvas()
    img = canvas.saveImage("predict.png")
    predict = model.predict(net,img)
    percentage = predict[1] * 100
    print(label_dict[predict[0]], f"{percentage:.2f}" + "%")
    