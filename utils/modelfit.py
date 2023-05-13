import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import torchvision
import torchvision.transforms as transforms
import model

net = model.createModel()

data_dir = r'C:\Users\pedro\OneDrive\Imagens\SymbolDataset'

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Carregando o conjunto de dados
dataset = ImageFolder(root=data_dir, transform=transform)

# Cria o DataLoader para o conjunto de treinamento e validação
trainloader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)
valloader = torch.utils.data.DataLoader(dataset, batch_size=4, shuffle=True)

# Define a função de perda e o otimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# Treina a rede por 10 épocas
for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # Obtém as entradas e os rótulos
        inputs, labels = data

        # Zera os gradientes
        optimizer.zero_grad()

        # Propagação para a frente e cálculo da perda
        outputs = net(inputs)
        loss = criterion(outputs, labels)

        # Propagação para trás e atualização dos pesos
        loss.backward()
        optimizer.step()

        # Imprime estatísticas da perda
        running_loss += loss.item()
        if i % 2000 == 1999:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Treinamento concluído!')
PATH = "./model.pth"
torch.save(net.state_dict(), PATH)