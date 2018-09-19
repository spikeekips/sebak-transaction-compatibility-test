package cases

import "github.com/ethereum/go-ethereum/rlp"

type textStruct struct {
	A string
	B string
	C string
	D string
}

type insideSerializableStruct struct {
	E string
	T textStruct
}

func test_TextStruct() []byte {
	t := textStruct{A: "showme", B: "findme", C: "killme", D: "eatme"}
	e, _ := rlp.EncodeToBytes(t)
	return e
}

func test_insideSerializableStruct() []byte {
	t := textStruct{A: "showme", B: "findme", C: "killme", D: "eatme"}
	i := insideSerializableStruct{E: "openme", T: t}
	e, _ := rlp.EncodeToBytes(i)
	return e
}

func init() {
	Cases["text_struct"] = test_TextStruct
	Cases["insideSerializable_struct"] = test_insideSerializableStruct
}
