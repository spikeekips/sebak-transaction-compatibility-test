package cases

import "github.com/ethereum/go-ethereum/rlp"

func CaseString() []byte {
	var e []byte
	e, _ = rlp.EncodeToBytes("showme")
	return e
}

func init() {
	Cases["string"] = CaseString
}
