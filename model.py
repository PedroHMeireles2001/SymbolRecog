import torch
import torch.nn as nn
import torchvision.transforms as transforms




# Define as dimensões da rede
input_size = 3 * 224 * 224 # 3 canais de cores, 224x224 pixels
hidden_size = 256
num_classes = 2 # número de classes no conjunto de dados

class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(MLP, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = nn.functional.relu(x)
        x = self.fc2(x)
        x = nn.functional.relu(x)
        x = self.fc3(x)
        return x
    
def createModel():
    return MLP(input_size, hidden_size, num_classes)

def loadModel(path):
    model = createModel()
    model.load_state_dict(torch.load(path))
    return model

def predict(net,img):
    img = transformImage(img)
    img = img.unsqueeze(0)
    with torch.no_grad():
        outputs = net(img)
    
    probabilities = torch.softmax(outputs, dim=1)
    _, predicted = torch.max(probabilities.data, 1)
    return predicted.item(), probabilities[0, predicted].item()


def transformImage(image):
    # Redimensiona a imagem
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    return transform(image)