# QR-CODE-Generator


## Pure python QR Code generator


## What is a QR Code?


A Quick Response code is a two-dimensional pictographic code used for its fast
readability and comparatively large storage capacity. The code consists of
black modules arranged in a square pattern on a white background. The
information encoded can be made up of any kind of data (e.g., binary,
alphanumeric, or Kanji symbols)

![image](https://user-images.githubusercontent.com/108206047/197936470-ad1b6024-4a32-4349-975e-ad49c3819d98.png)


### Generate QR codes.

A standard install uses pypng_ to generate PNG files and can also render QR
codes directly to the console. A standard install is just::

    pip install qrcode

### generate the code u can create the qr code

     import qrcode
     qr=qrcode.make("Enter your details\n")
     qr.save("qrcode.png")
     qr.show()
