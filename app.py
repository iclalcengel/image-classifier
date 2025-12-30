import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# CIFAR-10 sınıfları
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']

device = torch.device("cpu")

# train.py ile AYNI model
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 16, 3, 1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(16 * 30 * 30, 10)
        )

    def forward(self, x):
        return self.net(x)

model = SimpleCNN().to(device)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor()
])

st.title("Yapay Zeka Destekli Görüntü Sınıflandırıcı")

uploaded_file = st.file_uploader("Bir görüntü yükleyin", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Yüklenen Görüntü", use_column_width=True)

    if st.button("Tahmin Et"):
        img = transform(image).unsqueeze(0).to(device)
        with torch.no_grad():
            outputs = model(img)
            _, pred = torch.max(outputs, 1)

        st.success(f"Tahmin Edilen Sınıf: {classes[pred.item()]}")
