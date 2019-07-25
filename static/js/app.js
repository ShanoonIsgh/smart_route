var list = ["../white.jpeg","../red.png","../yellow.png","../green.png"]
var index = 0;
function changeLights() {
     index = index + 1;      
if (index == list.length) 
index = 0;      
var image = document.getElementById('light');     
image.src=list[index]; } 
  var timer = setInterval(changeLights,3000);