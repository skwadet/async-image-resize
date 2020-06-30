from django.test import TestCase
from resize_app import models


class ImageModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.ImageToResize.objects.create(image='/home/skwadet/Загрузки/6jkBOKh5BtE.jpg', width=200, height=200)

    def test_uuid_valid(self):
        image = models.ImageToResize.objects.all()[:1].get()
        uuid = image._meta.get_field('uuid').to_python(image.uuid)
        self.assertRegex(str(uuid), r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b')

    def test_image_max_width(self):
        image = models.ImageToResize.objects.all()[:1].get()
        max_width = image._meta.get_field('width').validators[0]
        self.assertEqual(max_width.limit_value, 9999)

    def test_image_max_height(self):
        image = models.ImageToResize.objects.all()[:1].get()
        max_height = image._meta.get_field('height').validators[0]
        self.assertEqual(max_height.limit_value, 9999)

    def test_image_min_width(self):
        image = models.ImageToResize.objects.all()[:1].get()
        min_width = image._meta.get_field('width').validators[1]
        self.assertEqual(min_width.limit_value, 1)

    def test_image_min_height(self):
        image = models.ImageToResize.objects.all()[:1].get()
        min_height = image._meta.get_field('width').validators[1]
        self.assertEqual(min_height.limit_value, 1)

    def test_date_valid(self):
        image = models.ImageToResize.objects.all()[:1].get()
        date = image._meta.get_field('date').auto_now
        self.assertEqual(date, 1)

    def test_status_max_length(self):
        image = models.ImageToResize.objects.all()[:1].get()
        max_length = image._meta.get_field('status').max_length
        self.assertEqual(max_length, 25)
