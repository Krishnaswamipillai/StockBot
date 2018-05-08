package main

import (
	"C"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
	"time"
)

//export FetchUrls
func FetchUrls(urls string) *C.char {
	urlList := strings.Split(urls, "|")
	ch := make(chan string)
	counter := 1
	responses := []string{}
	for _, url := range urlList {
		go func(url string) {
			resp, err := http.Get(url)
			if err != nil {
				return
			}
			if resp != nil {
				defer resp.Body.Close()
				body, _ := ioutil.ReadAll(resp.Body)
				ch <- string(body)
			}
		}(string(url))
	}
	for {
		select {
		case r := <-ch:
			responses = append(responses, r)
			if len(responses) == len(urlList) {
				return C.CString(strings.Join(responses, "||||||||||"))
			}
		case <-time.After(50 * time.Millisecond):
            fmt.Printf(".")
		}
	}
}

func main() {
}
