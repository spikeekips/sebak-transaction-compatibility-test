package cases

import (
	"github.com/ethereum/go-ethereum/rlp"
)

func CaseBytes() []byte {
	var e []byte
	e, _ = rlp.EncodeToBytes([]byte("showme"))

	return e
}

func init() {
	Cases["bytes"] = CaseBytes
}
