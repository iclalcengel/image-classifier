# Yapay Zeka Destekli Görüntü Sınıflandırıcı

## Proje Tanımı
Bu projede CIFAR-10 veri seti kullanılarak görüntüleri otomatik olarak
sınıflandırabilen bir yapay zeka uygulaması geliştirilmiştir. Sistem,
kullanıcı tarafından yüklenen görselleri ön işleme tabi tutarak
belirlenen sınıflardan birine ait olup olmadığını tahmin etmektedir.

## Hedef
Makine öğrenimi ve derin öğrenme teknikleri kullanılarak eğitilmiş bir
model aracılığıyla, yüklenen bir görselin hangi sınıfa ait olduğunu
tahmin eden kullanıcı dostu ve işlevsel bir sistem geliştirmek.

## Teknik Detaylar
- Proje PyTorch kütüphanesi kullanılarak geliştirilmiştir.
- CIFAR-10 veri seti ile model eğitimi gerçekleştirilmiştir.
- Görseller normalize edilmiş ve yeniden boyutlandırılmıştır.
- Model performansı accuracy, precision ve recall metrikleri ile
  değerlendirilmiştir.
- Kullanıcı arayüzü Streamlit kütüphanesi ile geliştirilmiştir.

## Kullanılan Veri Seti
CIFAR-10 veri seti  
(Uçak, otomobil, kuş, kedi, geyik, köpek, kurbağa, at, gemi ve kamyon
sınıflarını içermektedir.)

## Kurulum
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırınız:

```bash
pip install -r requirements.txt

Model Eğitimi

Modeli eğitmek için aşağıdaki komut çalıştırılır:

python train.py

Uygulamanın Çalıştırılması

Streamlit arayüzünü başlatmak için:

streamlit run app.py

Not

Model, sınırlı sayıda epoch ile eğitildiği için bazı sınıflandırma
sonuçlarında hatalar gözlemlenebilmektedir. Ancak sistem, görüntü
yükleme, ön işleme ve sınıflandırma fonksiyonlarını başarıyla yerine
getirmektedir.
