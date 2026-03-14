package main

import "fmt"
import "blockparser/block"

func main() {
	h := block.Header{
		Version:    1,
	}
	fmt.Printf("Block Header: %+v\n", h)
}