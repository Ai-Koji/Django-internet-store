isOpened = false

function openUrls(){
    console.log(2)
    if (!isOpened){
        document.querySelector(".urls").classList.remove("hidding-animation");
        isOpened = true;
    }
    
}

function closeUrls(){
    if (isOpened){
        console.log(document.querySelector(".urls"))
        document.querySelector(".urls").classList.add("hidding-animation");
        isOpened = false;
    }
}

// FORM

// open/close form
function openForm(formName){
    document.querySelector(`.${formName}`).classList.remove("hidden");
}
function closeForm(formName){
    document.querySelector(`.${formName}`).classList.add("hidden");
}
