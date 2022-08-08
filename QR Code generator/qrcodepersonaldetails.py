import qrcode
qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("Enter Your Name:")
age=int(input("Enter your age:"))
email=input("Enter your Email address:")
mobileno=int(input("Enter your Mobile number:"))
data={'Name':name,'Age':age,'Email':email,'Mobile':mobileno}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("MyDetails.png")
img.show()