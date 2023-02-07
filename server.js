const express = require ('express');
const {MongoClient, ServerApiVersion} = require('mongodb');
const path = require('path');
const bodyParser = require('body-parser');

const uri = "mongodb+srv://Anvil:SSSamalex3151@anvil.xrd9i2b.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri, {
    useNewUrlParser: true, 
    useUnifiedTopology: true, 
    serverApi: ServerApiVersion.v1 
});

const app = express();
const port = 3000;
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/public/login.html'));
});
app.listen(port, () => {
    console.log("Listening...");
})

const db = client.db('Anvil');
const users = db.collection('Users');
const forums = db.collection('Forums');

let account;

async function queryLogin(usernameInput) {
    let result = null;
    try {
        result = await users.findOne({username: usernameInput});
    } 
    catch{}
    // finally {
    //     await client.close();
    // }
    if(result == null)
        return {username: "FAIL_CODE"};
    else return result;
}

app.post('/login', (req, res) => {
    username = req.body.usernameInput;
    password = req.body.passwordInput;
    (async function () {
        const result = await queryLogin(username);
        account = result;
        if(result.username == "FAIL_CODE")
            res.send("Account not found");
        else if(result.password == password)
            res.sendFile(path.join(__dirname, '/public/dashboard.html'));
        else res.send("Incorrect password");
    })();
});

app.post('/forumPost', (req, res) => {
    res.send(req.body);
});

app.get('/initializeForum'), (req, res) => {
    (async function () {
        await initializeForum();
    })();
}

// function passwordHash(){
//     var hashObj = new jsSHA("SHA-512", "TEXT", {numRounds: 1});
//     hashObj.update(password.value);
//     var hash = hashObj.getHash("HEX");
//     generateJSON(hash);
// }

