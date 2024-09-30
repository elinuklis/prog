from PIL import Image

def bilde(datne):
    with Image.open(datne) as im:
        print(datne, im.format, f"{im.size}x{im.mode}")
        im.show()
        izmers = (b, c)
        im.thumbnail(izmers)
        im.save("bilde-maza.jpg", im.format)
        im.show

# def rediget(datne):
#     with Image.open(datne) as im:
#         im.show() .....

def rotate(datne):
    with Image.open(datne) as im:
        print(datne, im.format, f"{im.size}x{im.mode}")
        im.show()
        pagrieziens = im.rotate(90)
        pagrieziens.show()
        im.save("bilde-pagriezta-minions.jpg", im.format)
        im.show

a = input("Ievadi faila nosaukumu: ")
b = input("Ievadi pikseļu platumu: ")
c = input("Ievadi pikseļu garumu: ")
#rotate(a)
bilde(b, c)
