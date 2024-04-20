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

/*var title_change=document.getElementById('change_title');
document.addEventListener('mouseover',function(){
var message='Welcome Midori';
change_title.innerText=message;
change_title.style.color="Navy";
})
document.addEventListener('mouseout',function(){
var message='Welcome to my home';
change_title.innerText=message;
change_title.style.color="Black";
})*/
let image_url = [];
let turist_spot = [];
document.addEventListener('DOMContentLoaded', async function () {
  try {
    let buffer_image_url = [];
    
    let response = await fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1');
    let data = await response.json();
    //console.log(data);
    
    for (let i = 0; i < data.data.results.length; i++) {
        buffer_image_url = buffer_image_url.concat(data.data.results[i].filelist);
        turist_spot = turist_spot.concat(data.data.results[i].stitle);
        let regex = /https:\/\/.*?\.jpg/gi;
        let match = regex.exec(data.data.results[i].filelist);
        if (match) {
            let firstMatch = match[0];
            image_url = image_url.concat(firstMatch);
        } 
    }
    //console.log(image_url);
    //console.log(turist_spot);

      let imageContainers = document.querySelectorAll('.icon'); // 所有的 image container
      for (let i = 0; i < imageContainers.length; i++) {
          let imgElement = document.createElement('img');
          imgElement.src = image_url[i] || ''; // 確保圖片 URL 不為 undefined
          imgElement.className = 'icon';
          imageContainers[i].appendChild(imgElement); // 將圖片添加到對應的 image container 中
      }

      let pictureContainers = document.querySelectorAll(".pic_list .picture");
      for (let i = 0; i < pictureContainers.length; i++) {
          pictureContainers[i].style.backgroundImage = 'url(' + image_url[i+3] + ')' || ''; // 開始索引改為 3
      }
      let promotionText = document.querySelectorAll('.promotion [id^=\"text\"]');//選擇在promotion底下所有以text開頭的span
      for (let i=0;i<imageContainers.length;i++){
        let spanElement = document.createElement('span');
        let textNode = document.createTextNode(turist_spot[i]);
        spanElement.appendChild(textNode);
        promotionText[i].appendChild(spanElement);
        //textElements[i].classList.add('text');
      }
      
      let pictureElements = document.querySelectorAll('.title');
      for (let i=0;i<pictureContainers.length;i++){
        let spanElement1 = document.createElement('span');
        let textNode = document.createTextNode(turist_spot[i+3]);
        spanElement1.appendChild(textNode);
        pictureElements[i].appendChild(spanElement1);
        //textElements[i].classList.add('text');
      }
      //console.log(turist_spot); // 在這裡可以確保 image_url 有值
      //console.log(image_url);   
  } 
  catch (error) {
      console.log(`Error: ${error}`);
  }
});

setTimeout(function () {
  console.log(turist_spot); // 在這裡也顯示 turist_spot 的內容
  let pictureContainers = document.querySelectorAll(".pic_list .picture");
  let pictureContainer2 = document.getElementById("pic_list");
  function page_button(){
    for (let i=0;i<pictureContainers.length;i++){
      let divElement = document.createElement('div');
      divElement.className='picture';
      divElement.innerHTML = '<img class="star" src="star.png"><div class="title"></div>';
      pictureContainer2.appendChild(divElement);
      let newpictureContainers = document.querySelectorAll(".pic_list .picture");
      for (let j =0;j<newpictureContainers.length;j++){
        console.log('*****');
        newpictureContainers[i].style.backgroundImage = 'url(' + image_url[i+3] + ')' || '';
      }
      
    }  
} 
  
}, 2000); 
//console.log(turist_spot);
let dataContainer; // 在 root 範圍內定義一個空的變數

fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1')
  .then(response => response.json())
  .then(data => {
    dataContainer = data; // 將取得的資料賦值給 dataContainer
  })
  .catch(error => console.log(`Error: ${error}`));//定義一個空的變數，等fetch跑成功後才會把值傳給下面的button


let pictureContainers = document.querySelectorAll(".pic_list .picture");
let pictureContainer2 = document.getElementById("pic_list");
function page_button(){
  if (dataContainer){
  for (let i=0;i<pictureContainers.length;i++){
    let divElement = document.createElement('div');
    divElement.className='picture';
    divElement.innerHTML = '<img class="star" src="star.png"><div class="title"></div>';
    pictureContainer2.appendChild(divElement);
    let newpictureContainers = document.querySelectorAll(".pic_list .picture");
    
    for (let j =0;j<newpictureContainers.length;j++){
      newpictureContainers[j].style.backgroundImage = 'url(' + image_url[j+3] + ')' || '';
    }

    let pictureElements = document.querySelectorAll('.title');
    for (let j =0;j<pictureElements.length;j++){
      let spanElement1 = document.createElement('span');
      let textNode = document.createTextNode(turist_spot[j+3]);
      spanElement1.appendChild(textNode);
      if (pictureElements[j].innerText){
        continue;
      }
      else{
        pictureElements[j].appendChild(spanElement1);
      }
      
      //textElements[i].classList.add('text');
    }
  }}  
} 
