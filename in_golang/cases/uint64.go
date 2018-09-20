package cases

import "github.com/ethereum/go-ethereum/rlp"

func test_uint64(u uint64) []byte {
	var e []byte
	e, _ = rlp.EncodeToBytes(u)
	return e
}

func uint64_99() []byte {
	return test_uint64(uint64(99))
}

func uint64_max() []byte {
	return test_uint64(^uint64(0))
}

func init() {
	Cases["uint64_99"] = uint64_99
	Cases["uint64_max"] = uint64_max
}
