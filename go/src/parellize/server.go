package main

import (
    "net/http"
    "strings"
    "fmt"
    "encoding/json"
    "sync"
    "ioutil"
)

type WorkRequest struct {
    Function    string
    EncodedFunction string
    Parameter   string
}

type WorkResponse struct {
    Function string
    ResponseData string
}

type responseList struct {
    Mux sync.Mutex
    RespData []chan *WorkResponse
    RespKeys []string
}

var queue = make(chan *WorkRequest, 10000)
var responseLists *responseList

func sayHello(w http.ResponseWriter, r *http.Request) {
    message := r.URL.Path
    message = strings.TrimPrefix(message, "/")
    message = "Hello " + message
    w.Write([]byte(message))
}

func recieveData(w http.ResponseWriter, r *http.Request) {
    response := json.NewDecoder(r.Body)
    //Parse it, recieve functionName

}

func requestJob(w http.ResponseWriter, r *http.Request) {
    select {
        case workToDo := <-queue:
            w.Write([]byte(workToDo))
        default:
            fmt.Printf("queue appears to be empty!")
    }
}

func addGoJob(funcName, function, arguments){
    for _, item := range arguments {
        queue <- WorkRequest{Function: funcName, EncodedFunction: function, Parameter: item}
    }
}


func main() {
    http.HandleFunc("/returning", recieveData)
    http.HandleFunc("/addJob", addGoJob)
    http.HandleFunc("/requestJob", requestJob)
    if err := http.ListenAndServe(":8000", nil); err != nil {
        panic(err)
    }
}
