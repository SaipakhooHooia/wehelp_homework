fetch('https://www.google.com', {
      mode: 'no-cors'
    })
    .then((response) => {
      if (response.status != 200) {
        console.log('Yay ! connected');
        console.log(response);
      }
    }, (err) => {
      console.log('error: ' + err); 
  }, 5000);