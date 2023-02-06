console.log(data);

const userMsg = document.getElementById("chatContent");
const sendButton = document.getElementById("sendButton");
const forumIDContainer = document.getElementById("forumCode");
const forumNameContainer = document.getElementById("forumName");

const messageList = document.getElementById("chatBox");

const msgNumber = 0; //API call to most recent msgNumber++

const forumID = 12345;
const userID = 12345;
const forumName = "Test";

function loadMessages(){
    messageList.innerHTML += "World";
}

function sendMsg(message, forumID, msgNumber){
    const msgContent = userMsg.value;
    const json = [{"message": msgContent, "forumID": forumID, "userID": userID, "msgNumber": msgNumber}];
    //API send messages
    loadMessages();
}

function init(){
    loadMessages();
    forumNameContainer.innerHTML += forumName;
    forumIDContainer.innerHTML += forumID;
}

sendButton.addEventListener('click', sendMsg);

// document.onload(init());



