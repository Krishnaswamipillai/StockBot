                    
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
    var id_token = googleUser.getAuthResponse().id_token;
    console.log(id_token)
    xhttp.onload = function () {
        console.log(this.responseText);
        if (true) {
            //console.log(JSON.parse(this.responseText.stocks));
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
         var s = elem.innerHTML=xhttp.response
    };
    xhttp.open("POST", "/cgi-bin/stocks.py", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("ticker=" + ticker)
}

function getHistoricalStockData(ticker, startDate, endDate) {
    var xhttp = new XMLHttpRequest();

    xhttp.onload = function () {
        console.log(xhttp.response)

    };
    xhttp.open("POST", "/cgi-bin/stocks.py", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("ticker=" + ticker + "&startDate=" + startDate + "&endDate=" + endDate);
}