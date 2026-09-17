import qrcode
import sys
print(sys.executable)

url= "https://professional-portfolio-emph9jru76pocqxfmalnes.streamlit.app/"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=qrcode.constants.ERROR_CORRECT_M
)

qr.add_data(url)
qr.make(fit=True)  

img = qr.make_image(fill_color='black', back_color='white')
img.save('Resume.png')
