from django.test import TestCase
from .models import CommDisaster

# Create your tests here.
class ModelTest(TestCase):
    def test_can_insert_in_coomdisaster(self):
        disaster = CommDisaster()
        disaster.id = '0001112303'
        disaster.date = '2007-06-05 12:12:12'
        disaster.location = '530821102003'
        disaster.type='1'
        disaster.data= '23.132,102.307'
        disaster.structure='2'
        disaster.square='110'
        disaster.note=''
        disaster.reporting_unit='云南省人民政府办公厅' + '2'
        if disaster.pk is not None:
            disaster.delete()
        self.assertIsNone(disaster.pk)
        disaster.save()
        self.assertIsNotNone(disaster.pk)
        if disaster.pk is not None:
            disaster.delete()
        return
