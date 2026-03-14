package main
import (
		"encoding/hex"
		"fmt"
		"blockparser/block"
	)

func main() {
	h := block.Header{
		Version:    1,
	    Timestamp:1231006505,
	    Bits:0x1d00ffff,
	    Nonce:2083236893,
	}
    fmt.Printf("Block Header: %+v\n", h)
	data, err := hex.DecodeString("4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b")
	if err != nil {
		fmt.Println("Error decoding hex:", err)
		return
	}
	fmt.Printf("%x\n", data)
	fmt.Printf("Length: %d\n", len(data))
}