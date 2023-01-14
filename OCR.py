from PIL import Image
import pytesseract

def process_image(iamge_name):
    return pytesseract.image_to_string(Image.open(iamge_name))

def print_data(data):
    print(data)

def output_file(filename, data):
    file = open(filename, "w+")
    file.write(data)
    file.close()

def main():
    data_eng = process_image("image.png")
    print_data(data_eng)
    output_file("eng.txt", data_eng)

if  __name__ == '__main__':
    main()
