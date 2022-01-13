var requestURL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
var XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest; //when XMLHttpRequest not defined 
var xmlhttp= new XMLHttpRequest();

xmlhttp.open("GET",requestURL);
xmlhttp.responseType = 'json';
xmlhttp.send();

xmlhttp.onload = function(){
	var newImage = xmlhttp.response;
	addImage(newImage);
	showImage(newImage);
}

function addImage(jsonObj){
	var newImage = document.createElement('div');
	newImage.textContent = jsonObj['result']['results']['file'];
	div.appendChild(newImage);
}

function showImage(jsonObj){
	var Image = jsonObj['file'];

	for (i=0;i<Image.length;i++){
		var real_Image = document.createElement('div');
		real_Image.textContent = Image[i].file;
	}
	section.appendChild(real_Image);
}
console.log(xmlhttp)