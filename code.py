from PIL import Image as PILImage

class Image:
    @staticmethod
    def load(file):
        img = PILImage.open(file)
        img.show()
        return img

    @staticmethod
    def size(file):
        img = PILImage.open(file)
        width, height = img.size
        total_pixels = width * height
        return f"Pixels: {total_pixels} | Resolution: {width}x{height}"

    @staticmethod
    def type(file):
        img = PILImage.open(file)
        return img.format

filename = "photo.jpg"

Image.load(filename)
print(Image.size(filename))
print(f"Type: {Image.type(filename)}")
