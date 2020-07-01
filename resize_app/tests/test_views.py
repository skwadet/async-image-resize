import io
import tempfile

from PIL import Image
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from .. import models


class CreateImage:
    @staticmethod
    def new_image_for_api():
        file = io.BytesIO()
        new_image = Image.new('RGBA', size=(960, 640), color=(50, 50, 50))
        new_image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    @staticmethod
    def new_image_for_orm():
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        file = File(tmp_file)
        uploaded_file = SimpleUploadedFile('test.jpg', file.read(), content_type='multipart/form-data')
        return uploaded_file


class CreateTaskTestCase(APITestCase):

    def setUp(self):
        image = CreateImage.new_image_for_api()

        self.valid_data = {"image": image,
                           "height": 200,
                           "width": 200}

        self.invalid_data = {"image": image,
                             "height": 10000,
                             "width": 0}

    def test_create_task(self):
        response = self.client.post('/api/create/task/', data=self.valid_data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        response = self.client.post('/api/create/task/', data=self.invalid_data,
                                    format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetTestCase(APITestCase):
    def setUp(self):
        image = CreateImage.new_image_for_orm()
        models.ImageToResize.objects.create(image=image, width=200, height=200)

    def test_get_detailed_task(self):
        task = models.ImageToResize.objects.all()[:1].get()
        uuid = task._meta.get_field('uuid').to_python(task.uuid)
        response = self.client.get('/api/get/{uuid}/'.format(uuid=uuid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_list(self):
        response = self.client.get('/api/create/task/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
