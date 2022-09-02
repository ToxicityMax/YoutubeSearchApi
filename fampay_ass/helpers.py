import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible
from rest_framework.response import Response


def respond(status, message="", payload=False):
    response_json = {
        "message": message,
        "payload": payload
    }
    # if message:
    #     response_json['message'] = message
    # if payload:
    #     response_json['payload'] = payload
    #
    # if bool(response_json) is False:
    #     raise Exception("Either message or payload is required")

    return Response(response_json, status=status)


@deconstructible
class UploadTo(object):

    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        extension = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex[:12], extension)
        return os.path.join(self.path, filename)


def validate_image(image):
    file_size = image.file.size
    limit_mb = 20
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit)
