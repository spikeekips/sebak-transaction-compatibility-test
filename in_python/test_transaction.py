import unittest
import rlp
from rlp.sedes import (
    text,
    big_endian_int,
    List,
)

from .common import argon2_hash


class OperationHeader(rlp.Serializable):
    fields = (
        ('Type', text),
    )


class OperationBody(rlp.Serializable):
    fields = (
        ('Target', text),
        ('Amount', big_endian_int),
    )


class Operation(rlp.Serializable):
    fields = (
        ('H', OperationHeader),
        ('B', OperationBody),
    )


class TransactionHeader(rlp.Serializable):
    fields = (
        ('Version', text),
        ('Created', text),
        ('Hash', text),
        ('Signature', text),
    )


class TransactionBody(rlp.Serializable):
    fields = (
        ('Source', text),
        ('Fee', big_endian_int),
        ('SequenceID', big_endian_int),
        ('Operations', List((Operation,), False)),
    )


class TestTransactionRLPHash(unittest.TestCase):
    def makeTransactionBody(self):
        addresses = ('GBJSHCWIX2ZJOCRW4DA4W7SA7N5EAIUN47AJJKUR4YYVDCFUFEC6KJT2',)
        ops = list()
        for i in addresses:
            oph = OperationHeader(Type='payment')
            opb = OperationBody(Target=i, Amount=10)
            op = Operation(H=oph, B=opb)

            ops.append(op)

        tb = TransactionBody(
            Source='GBMVBVVBTXE2HR3FWRDBHPE2AURVLGZW7GBOFG47IVHR6TJZHJLNGJLH',
            Fee=10000,
            SequenceID=0,
            Operations=ops,
        )

        return tb

    def test_encoded_matched(self):
        expected = bytes(bytearray((
            248, 136, 184, 56, 71, 66, 77, 86, 66, 86, 86, 66, 84, 88, 69, 50, 72, 82, 51, 70, 87,
            82, 68, 66, 72, 80, 69, 50, 65, 85, 82, 86, 76, 71, 90, 87, 55, 71, 66, 79, 70, 71, 52,
            55, 73, 86, 72, 82, 54, 84, 74, 90, 72, 74, 76, 78, 71, 74, 76, 72, 130, 39, 16, 128,
            248, 72, 248, 70, 200, 135, 112, 97, 121, 109, 101, 110, 116, 248, 59, 184, 56, 71, 66,
            74, 83, 72, 67, 87, 73, 88, 50, 90, 74, 79, 67, 82, 87, 52, 68, 65, 52, 87, 55, 83, 65,
            55, 78, 53, 69, 65, 73, 85, 78, 52, 55, 65, 74, 74, 75, 85, 82, 52, 89, 89, 86, 68, 67,
            70, 85, 70, 69, 67, 54, 75, 74, 84, 50, 10,
        )))

        encoded = rlp.encode(self.makeTransactionBody())
        self.assertEqual(expected, encoded)

    def test_argon2_hash(self):
        expected = bytes(bytearray((
            130, 78, 199, 33, 20, 42, 41, 124, 240, 196, 194, 109, 118, 105, 46, 175, 11, 90,
            230, 98, 113, 71, 223, 201, 96, 95, 176, 151, 53, 126, 121, 198,
        )))

        encoded = rlp.encode(self.makeTransactionBody())
        self.assertEqual(expected, argon2_hash(encoded))
