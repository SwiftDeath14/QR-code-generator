import qrcode

# Data untuk QR Code
data = "https://vt.tokopedia.com/t/ZSjJtARTc/"  # Ganti dengan URL atau teks yang ingin Anda buat QR Code-nya

# Membuat QR Code
qr = qrcode.QRCode(
    version=1,  # Versi QR Code (1 hingga 40), semakin besar versi semakin kompleks
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Tingkat koreksi kesalahan (L, M, Q, H)
    box_size=10,  # Ukuran setiap kotak piksel QR Code
    border=4,  # Lebar border (harus minimal 4)
)

qr.add_data(data)  # Menambahkan data ke QR Code
qr.make(fit=True)  # Membuat QR Code dengan ukuran optimal

# Membuat gambar dari QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Menyimpan gambar ke file
img.save("qrcode_example.png")

print("QR Code berhasil dibuat dan disimpan sebagai 'qrcode_example.png'")
