fetch("https://script.google.com/macros/s/AKfycbwcwTJx861zYRsPsmhCBbcg9LFA_tPI289tGLW9WQOGSQs0YhGC1hjGmVkbL9svw1E2ZA/exec")
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));