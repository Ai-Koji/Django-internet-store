let form = document.querySelectorAll('#form-teg');

for (let index = 0; index != 2; index++) {
    console.log(index)
    form[index].addEventListener('submit', function(e) {
        e.preventDefault();
        if (!index) 
            formType = "service";
        else 
            formType = "question"
        fetch(`/send_form/${formType}`, {
            method: 'POST',
            body: new FormData(form[index])
        })
        .then(response => response.json())
        .then(data => {
            if (data == 200) 
                document.querySelectorAll("#form-send-success")[index].style.display = 'block';
            else 
                document.querySelectorAll("#form-send-error")[index].style.display = 'block';
            submit = document.querySelectorAll("#submit-button")[index]
            submit.disabled = true
            submit.classList.add('submit-disabled')
        })
        .catch(error => {
            console.error(error);
        })
    });
}