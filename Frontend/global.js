// const lambda = require("lambda-api");

function getInfo(event){
    // const query = searchInput.value;
    let url = 'https://q5e2sgn55a.execute-api.us-east-1.amazonaws.com/default/anvil';
        fetch(url, {
        method: 'GET'})
        .then(response => response.json())
        .then(console.log(response));
}

getInfo();

