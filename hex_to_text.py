import binascii
import gzip
import io

hex_data = ""

with open("hex","r") as f:
    hex_data = f.read()

print(len(hex_data.replace("\n", "").split(",")))
# Hexadecimal veriyi temizle ve byte dizisine dönüştür
hex_data = hex_data.replace("\n", "").replace("0x", "").replace(",", "").replace(" ", "")
byte_data = binascii.unhexlify(hex_data)

# Byte dizisini gzip formatından çıkar
with gzip.GzipFile(fileobj=io.BytesIO(byte_data)) as f:
    decompressed_data = f.read()

# Çıkarılan veriyi metin formatına dönüştür
text_data = decompressed_data.decode('utf-8')

with open("server.html","w") as f:
    f.write(text_data)

print(len(text_data.split(",")))