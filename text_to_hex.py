import gzip
import binascii
import io

# Orijinal metin verisi
text_data = ""

with open("server.html","r")  as f:
    text_data = f.read()


# Metin verisini gzip ile sıkıştır
buffer = io.BytesIO()
with gzip.GzipFile(fileobj=buffer, mode='w') as f:
    f.write(text_data.encode('utf-8'))

compressed_data = buffer.getvalue()

# Sıkıştırılmış veriyi hexadecimal formatına çevir
hex_data = binascii.hexlify(compressed_data).decode('utf-8')

# Okunabilirlik açısından hexadecimal veriyi formatla
formatted_hex_data = ', '.join(['0x' + hex_data[i:i+2] for i in range(0, len(hex_data), 2)])

# Çıktıyı daha temiz hale getirmek için satır sonu ekleyelim
formatted_hex_data_with_newlines = '\n'.join([formatted_hex_data[i:i+48] for i in range(0, len(formatted_hex_data), 48)])

with open("hex","w") as f:
    f.write(formatted_hex_data_with_newlines)
print(len(formatted_hex_data_with_newlines.replace("\n", "").split(",")))
