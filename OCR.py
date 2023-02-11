from PIL import Image
import pytesseract
import re

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    try:
        result = re.search(r"([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])",text).group(0)
        return result
    except:
        return "Image is not clear. Rescan the image"

#def print_data(data):
   # print(data)

#def output_file(filename, data):
 #   file = open(filename, "w+")
  #  file.write(data)
   # file.close()

#def main():
 #   data_eng = process_image("image.png")
  #  print_data(data_eng)
   # output_file("eng.txt", data_eng)

#if  __name__ == '__main__':
 #   main()

#with open('ocr.pkl', 'wb') as file:
#    pickle.dump(text, file)
