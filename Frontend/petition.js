const payIssue = document.getElementById("grievance1");
const hoursIssue = document.getElementById("grievance2");
const safetyIssue = document.getElementById("grievance3");
const harassmentIssue = document.getElementById("grievance4");
const cultureIssue = document.getElementById("grievance5");
const PTOIssue = document.getElementById("grievance6");

const userID = 12345;
const forumID = 12345;

const UserGrievancesExist = false;

const sendButton = document.getElementById("sendButton");

sendButton.addEventListener('click', exportGrievances);

function exportGrievances(){
    const json = [{
        "pay": payIssue.checked,
        "hours": hoursIssue.checked,
        "safety": safetyIssue.checked,
        "harassment": harassmentIssue.checked,
        "culture": cultureIssue.checked,
        "PTO": PTOIssue.checked
    }];
    setUserGrievances(json);
}

function setUserGrievances(json){
    //if UserGrievances dont exist yet, set these grievances
    setForumGrievaces(json);
}

function setForumGrievaces(json){   
    
}

function check(element){
    if (element.src = "circle-svgrepo-com.svg"){
        element.src = "check-circle-svgrepo-com.svg";
    }
    else if (element.src = "check-circle-svgrepo-com.svg")
        element.src = "circle-svgrepo-com.svg";
}

payIssue.addEventListener('click', () => check(payIssue));
hoursIssue.addEventListener('click', () => check(hoursIssue));
safetyIssue.addEventListener('click', () => check(safetyIssue));
harassmentIssue.addEventListener('click', () => check(harassmentIssue));
cultureIssue.addEventListener('click', () => check(cultureIssue));
PTOIssue.addEventListener('click', () => check(PTOIssue));









