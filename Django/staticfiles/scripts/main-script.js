
// mobile urls
let isOpenLinkedPage = true;
function openCloseCoverLinkedToPage(){
    let pages = document.querySelector('.pages');
    let carpetClose = document.querySelector('.carpet-close').style;

    if (isOpenLinkedPage) {
        pages.style.display = 'block';
        carpetClose.display = 'block';
    }
    else {
        pages.classList.add('hidding-animation')
        setTimeout(function() {
            pages.style.display = 'none';
            pages.classList.remove('hidding-animation')
            carpetClose.display = 'none';
        }, 1000)
    }
    isOpenLinkedPage = !isOpenLinkedPage;
}

window.addEventListener('resize', function() {
    if (window.innerWidth > 1000) {
        document.querySelector('.pages').style.display = 'block';
    }
    if (window.innerWidth < 1000) {
        document.querySelector('.pages').style.display = 'none';
    }
});

// FORM

// open/close form
function openForm(formName){
    document.querySelector(`.${formName}`).classList.remove("hidden")
}
function closeForm(formName){
    document.querySelector(`.${formName}`).classList.add("hidden")
}
