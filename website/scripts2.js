                    
function onSignIn(googleUser, fillInfo) {
    var xhttp = new XMLHttpRequest();
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); 
    console.log('Name: ' + profile.getName());
    document.querySelector(".name").innerHTML=profile.getName()
    console.log('Image URL: ' + profile.getImageUrl());
    document.getElementById("userImage").setAttribute("src", profile.getImageUrl())
    console.log('Email: ' + profile.getEmail());
    document.querySelector(".email").innerHTML=profile.getEmail()
    id_token = googleUser.getAuthResponse().id_token;
    console.log(id_token)
    xhttp.onload = function () {
        if (this.responseText != null) {
            stocks = JSON.parse(this.responseText)['stocks'];
            for (i in stocks){
                addcard(i)
            }
        }
    };
    xhttp.open("POST", "/cgi-bin/main.py", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("clientId=" + id_token);
}

function getCurrentStockPrice(ticker, elem){
    var xhttp = new XMLHttpRequest();

     xhttp.onload = function () {
         console.log(xhttp.response)
         elem.innerHTML = this.responseText
    };
    xhttp.open("POST", "/cgi-bin/stockhandler.py", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("ticker=" + ticker)
}

function getHistoricalStockData(ticker) {
    var xhttp = new XMLHttpRequest();

    xhttp.onload = function () {
        if (this.responseText != null){

            data = JSON.parse(this.responseText)
            console.log(data)

            for(i in data){
                data[i].push(Date.parse(data[i][1]).getTime())

            }
            graphHD(data, 4528, "graph", 4528)

        }
    };
    xhttp.open("POST", "/cgi-bin/historicalstock.py", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("ticker=" + ticker);
}