import subprocess
import rlp
from rlp.sedes import text


def p(b):
    return ' '.join(map(str, (b)))


def test_bytes():
    a = 'showme'.encode('utf-8')
    b = rlp.encode(a)
    return p(b)


def test_string():
    a = 'showme'
    b = rlp.encode(a)
    return p(b)


def test_uint64_99():
    a = 99
    b = rlp.encode(a)
    return p(b)


def test_uint64_max():
    a = 18446744073709551615
    b = rlp.encode(a)
    return p(b)


class textStruct(rlp.Serializable):
    fields = (
        ('A', text),
        ('B', text),
        ('C', text),
        ('D', text),
    )


def test_text_struct():
    b = rlp.encode(textStruct(A='showme', B='findme', C='killme', D='eatme'))
    return p(b)


class insideSerializableStruct(rlp.Serializable):
    fields = (
        ('E', text),
        ('T', textStruct),
    )


def test_insideSerializable_struct():
    t = textStruct(A='showme', B='findme', C='killme', D='eatme')
    i = insideSerializableStruct(E='openme', T=t)
    b = rlp.encode(i)
    return p(b)


cases = (
    'bytes',
    'string',
    'uint64_99',
    'uint64_max',
    'text_struct',
    'insideSerializable_struct',
)

for case in cases:
    f = globals()['test_%s' % case]
    in_python = f()
    o = subprocess.run(['go', 'run', 'go/main.go', case], stdout=subprocess.PIPE)
    in_golang = o.stdout.decode('utf-8').strip()

    print(case, in_python == in_golang)
