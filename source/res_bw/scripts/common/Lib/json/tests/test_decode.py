# Python bytecode 2.6 (decompiled from Python 2.7)
# Embedded file name: scripts/common/Lib/json/tests/test_decode.py
# Compiled at: 2010-08-25 17:58:21
import decimal
from unittest import TestCase
import json

class TestDecode(TestCase):

    def test_decimal(self):
        rval = json.loads('1.1', parse_float=decimal.Decimal)
        self.assert_(isinstance(rval, decimal.Decimal))
        self.assertEquals(rval, decimal.Decimal('1.1'))

    def test_float(self):
        rval = json.loads('1', parse_int=float)
        self.assert_(isinstance(rval, float))
        self.assertEquals(rval, 1.0)
