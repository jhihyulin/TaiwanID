import unittest
from taiwanid import TaiwanID


class TestTaiwanID(unittest.TestCase):
    def setUp(self):
        self.taiwan_id = TaiwanID()

    def test_validate_success(self):
        self.assertEqual(self.taiwan_id.validate('A123456789'), self.taiwan_id.ValidateStatus.SUCCESS)

    def test_validate_length(self):
        self.assertEqual(self.taiwan_id.validate('A12345678'), self.taiwan_id.ValidateStatus.LENGTH_ERROR)

    def test_validate_format(self):
        self.assertEqual(self.taiwan_id.validate('0123456789'), self.taiwan_id.ValidateStatus.FORMAT_ERROR)
        self.assertEqual(self.taiwan_id.validate('A12345678A'), self.taiwan_id.ValidateStatus.FORMAT_ERROR)

    def test_validate_check(self):
        self.assertEqual(self.taiwan_id.validate('A123456780'), self.taiwan_id.ValidateStatus.CHECK_ERROR)

    def test_get_city_A(self):
        self.assertEqual(self.taiwan_id.get_city('A123456789').name, '臺北市')

    def test_get_city_E(self):
        self.assertEqual(self.taiwan_id.get_city('E123456789').name, '高雄市')

    def test_get_city_Y(self):
        self.assertEqual(self.taiwan_id.get_city('Y123456789').name, '陽明山管理局')

    def test_get_city_index_error(self):
        with self.assertRaises(IndexError):
            self.taiwan_id.get_city('.123456789')

    def test_get_gender_female(self):
        self.assertEqual(self.taiwan_id.get_gender('A223456789'), self.taiwan_id.Genders.Female)
        self.assertEqual(type(self.taiwan_id.get_gender('A223456789')), type(self.taiwan_id.Genders.Gender))
        self.assertEqual(self.taiwan_id.get_gender('A923456789'), self.taiwan_id.Genders.Female)
        self.assertEqual(type(self.taiwan_id.get_gender('A923456789')), type(self.taiwan_id.Genders.Gender))

    def test_get_gender_male(self):
        self.assertEqual(self.taiwan_id.get_gender('A123456789'), self.taiwan_id.Genders.Male)
        self.assertEqual(type(self.taiwan_id.get_gender('A123456789')), type(self.taiwan_id.Genders.Gender))
        self.assertEqual(self.taiwan_id.get_gender('A823456789'), self.taiwan_id.Genders.Male)
        self.assertEqual(type(self.taiwan_id.get_gender('A823456789')), type(self.taiwan_id.Genders.Gender))

    def test_get_gender_value_error(self):
        with self.assertRaises(ValueError):
            self.taiwan_id.get_gender('A323456789')

    def test_get_citizenship_native(self):
        self.assertEqual(self.taiwan_id.get_citizenship('A123456789'), self.taiwan_id.Citizenship.NATIVE)
        self.assertEqual(self.taiwan_id.get_citizenship('A223456789'), self.taiwan_id.Citizenship.NATIVE)

    def test_get_citizenship_foreign(self):
        self.assertEqual(self.taiwan_id.get_citizenship('A823456789'), self.taiwan_id.Citizenship.FOREIGN)
        self.assertEqual(self.taiwan_id.get_citizenship('A923456789'), self.taiwan_id.Citizenship.FOREIGN)

    def test_get_citizenship_value_error(self):
        with self.assertRaises(ValueError):
            self.taiwan_id.get_citizenship('A723456789')

    def test_get_naturalization_national(self):
        self.assertEqual(self.taiwan_id.get_naturalization('A123456789'), self.taiwan_id.Naturalization.NATIONAL)
        self.assertEqual(self.taiwan_id.get_naturalization('A223456789'), self.taiwan_id.Naturalization.NATIONAL)

    def test_get_naturalization_formerly_foreign(self):
        self.assertEqual(self.taiwan_id.get_naturalization('A163456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_FOREIGN)
        self.assertEqual(self.taiwan_id.get_naturalization('A263456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_FOREIGN)

    def test_get_naturalization_formerly_without_household_registration(self):
        self.assertEqual(self.taiwan_id.get_naturalization('A173456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_WITHOUT_HOUSEHOLD_REGISTRATION)
        self.assertEqual(self.taiwan_id.get_naturalization('A273456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_WITHOUT_HOUSEHOLD_REGISTRATION)

    def test_get_naturalization_formerly_hongkong_or_macao_resident(self):
        self.assertEqual(self.taiwan_id.get_naturalization('A183456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_HONGKONG_OR_MACAO_RESIDENT)
        self.assertEqual(self.taiwan_id.get_naturalization('A283456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_HONGKONG_OR_MACAO_RESIDENT)

    def test_get_naturalization_formerly_china_resident(self):
        self.assertEqual(self.taiwan_id.get_naturalization('A193456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_CHINA_RESIDENT)
        self.assertEqual(self.taiwan_id.get_naturalization('A293456789'), self.taiwan_id.Naturalization.NATIONAL_FORMERLY_CHINA_RESIDENT)

    def test_get_naturalization_non_national(self):
        self.assertEqual(self.taiwan_id.get_naturalization('A823456789'), self.taiwan_id.Naturalization.NON_NATIONAL)
        self.assertEqual(self.taiwan_id.get_naturalization('A923456789'), self.taiwan_id.Naturalization.NON_NATIONAL)

if __name__ == '__main__':
    unittest.main(verbosity=2)
