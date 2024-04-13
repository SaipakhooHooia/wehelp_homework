function clickMe() {
    console.log("Open");
      var dropdown = document.getElementById("Dropdown");
      if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
        
      } else {
        dropdown.style.display = "block";
      }
    }
    function clickMe2() {
    console.log("Close");
      var dropdown = document.getElementById("Dropdown");
        dropdown.style.display = "none";
    }

var title_change=document.getElementById('change_title');
document.addEventListener('mouseover',function(){
var message='Welcome Midori';
change_title.innerText=message;
change_title.style.color="Navy";
})
document.addEventListener('mouseout',function(){
var message='Welcome to my home';
change_title.innerText=message;
change_title.style.color="Black";
})