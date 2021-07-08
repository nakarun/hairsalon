from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

import datetime
import pytz

from accounts.models import CustomerUser
from hairsalon.models import Salon
from ..models import PointCard, Stamp
from ..views import get_stamp_frames


class TestPointCardView(TestCase):

    def setUp(self):
        """
        テストユーザー、テスト美容室、テストポイントカード、テストスタンプの作成
        """
        self.testsalon = Salon.objects.create(name='testsalon')
        self.testpointcard = PointCard.objects.create(
            salon=self.testsalon, vertical_cells_count=2, horizontal_cells_count=5)
        self.testuser = CustomerUser.objects.create_user(username='testuser', password='pass')
        stamps = []
        for d in range(1, 12):
            stamp = Stamp(
                customer=self.testuser,
                pointcard=self.testpointcard,
                stamped_at=datetime.date(2021, d, 1),
            )
            if d == 3:
                stamp.is_already_used = True
            stamps.append(stamp)
        self.created_stamps = Stamp.objects.bulk_create(stamps)

    def test_get_stamp_frames_method(self):
        """
        PointCardとStampsを渡すとPointCard.vertical_cells_count x PointCard.horizontal_cells_countの二次元配列を返してくれる
        """
        stamps = Stamp.unused_objects.filter(customer=self.testuser, pointcard=self.testpointcard)
        stamp_frames = get_stamp_frames(self.testpointcard, stamps)
        self.assertEqual(len(stamp_frames), self.testpointcard.vertical_cells_count)
        self.assertEqual(len(stamp_frames[0]), self.testpointcard.horizontal_cells_count)

        # is_already_used==Trueの3月のスタンプがないことを確認
        checked_dates = [[1, 2, 4, 5, 6], [7, 8, 9, 10, 11]]
        for stamp_v, d_v in zip(stamp_frames, checked_dates):
            for stamp_h, d_h in zip(stamp_v, d_v):
                self.assertEqual(stamp_h.stamped_at.month, d_h)

    def test_get_without_login(self):
        """
        ログインせずにアクセスするとログインページにリダイレクトされることを確認
        """
        response = self.client.get(reverse('pointcard'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/pointcard/')

    def test_get(self):
        """
        ログインしてアクセスすると無事ステータスコード200が返されることを確認
        """
        # テストクライアントでログインをシミュレート
        logged_in = self.client.login(username=self.testuser.username, password='pass')
        # ログインできたか確認
        self.assertTrue(logged_in)
        response = self.client.get(reverse('pointcard'))
        self.assertEqual(response.status_code, 200)
