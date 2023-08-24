//mobile adapt for .header-urls

function handleResize() {
    if (window.innerWidth <= 1001){
        document.querySelector('.open-urls-modile-button').style.display = "block";
        document.querySelector('.header-urls').style.transform = "translateX(-100%)";
        setTimeout(() => {
            document.querySelector('.header-urls').style.transition = "all 0.5s";
        }, 10);
    }
    else {
        document.querySelector('.open-urls-modile-button').style.display = "none";
        document.querySelector('.header-urls').style.transform = "";
        document.querySelector('.header-urls').style.transition = "";
    }
}


handleResize();
window.addEventListener('resize', handleResize);

let isOpened = false;

function openUrls() {
    if (!isOpened){
        document.querySelector('.header-urls').style.transform = "translateX(0%)";
        isOpened = true
    }
}
function closeUrls() {
    if (isOpened){
        document.querySelector('.header-urls').style.transform = "translateX(-100%)";
        isOpened = false
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
// hide loader
    window.addEventListener('load', function() {
    document.getElementById('loader').style.opacity = 0;
    setTimeout(function() {
        document.getElementById('loader').style.display = 'none';
    }, 500);
});