try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import cv2
from nltk.tokenize import word_tokenize

def extract_text_from_image(file_):
    img = Image.open(file_)
    text = pytesseract.image_to_string(img)
    tokenized_text = word_tokenize(text)
    
    name = []
    address = []
    dob = []
    dlId = []
    nameFlag = False
    addressFlag = False
    dobFlag = False
    dlIdFlag = False
    for word in tokenized_text:
        if word == 'Name':
            nameFlag = True
        if word == 'S/DW':
            nameFlag = False
        if word == 'Address':
            addressFlag = True
        if word == 'Femp':
            addressFlag = False
        if word == '»':
            dobFlag = True
        if word == 'BG':
            dobFlag = False
        if word == 'D.L.No':
            dlIdFlag = True
        if word == 'Name':
            dlIdFlag = False
        if nameFlag == True and word != 'Name':
            name.append(word)
        if addressFlag == True and word != 'Address':
            address.append(word)
        if dobFlag == True and word != '»':
            dob.append(word)
        if dlIdFlag == True and word != 'D.L.No':
            dlId.append(word)
    response = {}
    response['name'] = ' '.join(name)
    response['address'] = ' '.join(address)
    response['dob'] = ' '.join(dob)
    response['dlId'] = ' '.join(dlId)

    return response