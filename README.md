# Yapay Zeka Destekli G�r�nt� S�n�fland�r�c�

## Proje Tan�m�
Bu projede CIFAR-10 veri seti kullan�larak g�r�nt�leri otomatik olarak s�n�fland�rabilen
bir yapay zeka uygulamas� geli�tirilmi�tir.

## Hedef
Makine ��renimi teknikleri ile e�itilmi� bir model kullanarak, y�klenen bir g�rselin
hangi s�n�fa ait oldu�unu tahmin eden kullan�c� dostu bir sistem geli�tirmek.

## Teknik Detaylar
- PyTorch ile ResNet18 modeli kullan�lm��t�r.
- G�rseller normalize edilmi� ve yeniden boyutland�r�lm��t�r.
- Model performans� accuracy, precision ve recall metrikleri ile �l��lm��t�r.
- Aray�z Streamlit ile geli�tirilmi�tir.

## Kullan�lan Veri Seti
CIFAR-10 veri seti (u�ak, araba, hayvan ve nesne s�n�flar�)

## �al��t�rma
```bash
pip install -r requirements.txt
python train.py
streamlit run app.py
