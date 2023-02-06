let express = require ('express');
const path = require('path');
let bodyParser = require('body-parser');
// let fetch = require('node-fetch');

let app = express();
const port = 3000;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/public/login.html'));
});


// function passwordHash(){
//     var hashObj = new jsSHA("SHA-512", "TEXT", {numRounds: 1});
//     hashObj.update(password.value);
//     var hash = hashObj.getHash("HEX");
//     generateJSON(hash);
// }



app.post('/login', (req, res) => {
    if(req.body.usernameInput == "sam" && req.body.passwordInput =="tomack"){
        res.send("SUCCESS");
    }
    else
        res.send('FAIL');
});

app.post('/forumPost', (req, res) => {
    res.send(req.body.messageInput);
});

app.listen(port, () => {
    console.log("Listening...");
})