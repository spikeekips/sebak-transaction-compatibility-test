package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/spikeekips/sebak-transaction-compatibility-test/go/cases"
)

func b2s(t string, e []byte) {
	var s string
	for _, i := range e {
		s += fmt.Sprintf("%d ", i)
	}

	s = strings.TrimSpace(s)
	fmt.Println(s)
}

func main() {
	if len(os.Args) < 2 {
		os.Exit(1)
	}

	cs := os.Args[1:]

	for _, c := range cs {
		e := cases.Cases[c]()
		b2s(c, e)
	}
}
