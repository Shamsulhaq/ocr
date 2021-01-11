from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
import tesserocr
from PIL import Image
from rest_framework import views, status


class OrcApiView(views.APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file = request.data['file']
        image = Image.open(file)
        text = tesserocr.image_to_text(image)
        text = text.split("\n")
        return Response(data={"text": text}, status=status.HTTP_200_OK)



