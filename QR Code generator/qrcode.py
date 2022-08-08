import qrcode
qr=qrcode.make("Name=Kokkirala Abhinav\n studing=B.Tech\n age=19 years\n mobile no=9110776421\n")
qr.save("qrcode.png")
qr.show()

