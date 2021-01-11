from tesserocr import PyTessBaseAPI, RIL
import tesserocr
from PIL import Image
'''
print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('sample.png')
print(tesserocr.image_to_text(image))  # print from Image file
print(tesserocr.file_to_text('sample.png')) # print from File
'''

image = Image.open('sample1.png')
with PyTessBaseAPI() as api:
	api.SetImage(image)
	boxes = api.GetComponentImages(RIL.TEXTLINE, True)
	print('Found {} textline image components.'.format(len(boxes)))
	for i,(im,box,_,_) in enumerate(boxes):
		api.SetRectangle(box['x'],box['y'],box['w'],box['h'])
		ocrResult = api.GetUTF8Text()
		conf = api.MeanTextConf()
		print(u"Box[{0}]: x={x}, y={y}, w={w}, h={h}, "
              "confidence: {1}, text: {2}".format(i, conf, ocrResult, **box))


