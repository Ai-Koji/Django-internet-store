const form = document.querySelector('#form');

form.addEventListener('submit', async function(e) {
  e.preventDefault();
  const formData = new FormData(form); 

  try {
    const response = await fetch(form.action, {
      method: 'POST',
      body: formData
    });
    const data = await response.text();
    if (data == 200){
        document.querySelector('#form-send-success').style.display = 'block';
        document.querySelector('#submit-button').disabled = true;
    }
    else
        document.querySelector('#form-send-error').style.display = 'block'
  } 
  catch (error) {
    console.error(error);
    document.querySelector('#form-send-error').style.display = 'block'
  }
});