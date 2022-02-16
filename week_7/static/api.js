const myForm = document.getElementById("js-search")
myForm.addEventListener('submit', function(ev) {
ev.preventDefault();
const formData = new FormData(myForm);
const queryString = new URLSearchParams(formData);
let change=document.getElementById("hereIsResult");
fetch('http://127.0.0.1:3000/api/members?' + queryString, {
    method:'GET',
 })
    .then(res => res.json())
    .then(res=>{
        change.innerHTML=res.data.name+"("+res.data.username+")";
    })
    .catch(error => change.innerHTML="no result Q.Q");
});

const newName = document.getElementById("js-rename");
newName.addEventListener('submit', function(ev) {
ev.preventDefault();
const nameData = new FormData(newName);
const jsonData = Object.fromEntries(nameData.entries()) //convert entried data into object
let show=document.getElementById("reName");
fetch('http://127.0.0.1:3000/api/member', {
    method:'POST',
    body: JSON.stringify(jsonData), //only method"POST" has body
    //add "" into JSON, convert object into JSON
    headers: new Headers({
        "Content-Type":"application/json"
    })
}).then(res => res.json())
.then(res => {show.innerHTML="更新成功!"})
.catch(error => console.error('Error:', error));
})
