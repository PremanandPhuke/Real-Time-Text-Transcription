# import flask
from flask import Flask, render_template
import cv2

app= Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

# app= Flask(__name__)
@app.route("/start")
def start():
    import cv2
    from PIL import Image
    from pytesseract import pytesseract

    camera=cv2.VideoCapture(0)
    f=open("Output.txt", 'a')

    while True:
        _,image=camera.read()
        cv2.imshow('Text Detection', image)
        if cv2.waitKey(1)& 0xFF==ord('s'):
            cv2.imwrite('test1.jpg', image)
            break
    camera.release()
    cv2.destroyAllWindows()

  
    path_to_tesseract= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath='test1.jpg'
    pytesseract.tesseract_cmd=path_to_tesseract
    text=pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])

    f.write("------------------------------------------------\n")
    f.write(text[:-1])
    f.write("------------------------------------------------\n")
    data=text[:-1]
    f.close()
    
    return render_template('output.html', data=data)    

app.run(debug=True)