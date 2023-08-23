// slider

let prevSlideId = 1, 
    slideID = 1,
    slides = document.querySelectorAll(".slide"),
    buttons = document.querySelectorAll('#slide-button');


// function for change slide with id
function changeSlide () {
    for (let index = 0; index < slides.length; index++) {
        slides[index].style.transform = `translateX(-${100 * (slideID - 1)}%)`
    }
    buttons[prevSlideId - 1].classList.remove("active-button");
    prevSlideId = slideID;
    buttons[prevSlideId - 1].classList.add("active-button");
    
}

function changeActiveForButtons() {

}


function nextSlide(){
    slideID++;
    if (slideID > slides.length)
        slideID = 1;
    changeSlide();
}

function prevSlide() {    
    slideID--;
    if (slideID <= 0)
        slideID = slides.length;
    changeSlide();
}

function slide(slideId) {
    slideID = slideId;
    changeSlide();
}
