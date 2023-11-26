import requests
from PIL import Image
import io
import base64

# Örnek bir resim dosyasını aç
image_path = "demo.jpg"
image = Image.open(image_path)

# Resmi bir bytes nesnesine çevir
image_bytes = io.BytesIO()
image.save(image_bytes, format='JPEG')
image_bytes = image_bytes.getvalue()

# Flask uygulamasının çalıştığı adresi ve portu belirt
api_url = "http://127.0.0.1:5002/process_image"


files = {'image': ('image.jpg', image_bytes, 'image/jpeg')}
country={"country":"US"}
response = requests.post(api_url, files=files,data=country)

# İşlemin başarılı olup olmadığını kontrol et
if response.status_code == 200:
    # Base64 encoded olarak alınan resmi kaydet
    image_data = response.json()['image_data']
    with open("output_image1.png", "wb") as f:
        f.write(base64.b64decode(image_data))
    print("İşlem başarıyla tamamlandı. Oluşturulan resim 'output_image.png' olarak kaydedildi.")
else:
    print("Hata:", response.json())
