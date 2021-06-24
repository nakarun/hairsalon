from django.test import TestCase
from django.contrib.auth import get_user_model

from datetime import datetime
import pytz

from hairsalon.models import Salon
from ..models import PointCard, Stamp


class TestPointCardModel(TestCase):

    def setUp(self):
        """
        テストユーザー、テスト美容室、テストポイントカード、テストスタンプの作成
        """
        self.testsalon = Salon.objects.create(name='testsalon')
        self.testpointcard = PointCard.objects.create(
            salon=self.testsalon, vertical_cells_count=2, horizontal_cells_count=5)
        self.testuser = get_user_model().objects.create_user(username='testuser', password='pass')
        stamps = []
        for d in range(1, 12):
            stamp = Stamp(
                customer=self.testuser,
                salon=self.testsalon,
                stamped_at=datetime(2021, d, 1, 12, 0, 0, 0, pytz.timezone('Asia/Tokyo'))
            )
            if d == 3:
                stamp.is_already_used = True
            stamps.append(stamp)
        self.created_stamps = Stamp.objects.bulk_create(stamps)

    def test_stamp_unused_objects(self):
        """
        unused_objectsで取得すると、is_already_used==Trueの3月のスタンプがないことを確認
        """
        stamps = Stamp.unused_objects.filter(customer=self.testuser, salon=self.testsalon, stamped_at__month=3)
        self.assertEqual(stamps.count(), 0)
