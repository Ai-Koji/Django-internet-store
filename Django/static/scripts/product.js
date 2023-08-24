// hide slider buttons for slider with 1 slide
arrowPrev = document.querySelectorAll(".arrow-prev")
arrowNext = document.querySelectorAll(".arrow-next")

// first slider
sliderCount = document.querySelectorAll("#main-img-slide").length;
if (sliderCount == 1) {
    arrowPrev[0].style.display = "none";
    arrowNext[0].style.display = "none";
}

// second slider
sliderCount = document.querySelectorAll(".img-slide").length;
if (sliderCount == 1) {
    arrowPrev[1].style.display = "none";
    arrowNext[1].style.display = "none";
}

// hide the second slider if it's clean
if (sliderCount == 0) {
    document.querySelector("#button-3").style.display = "none";
}



// Offer
function openOffer(){
    document.querySelector(".Offer").classList.remove("hidden")
}
function closeOffer(){
    document.querySelector(".Offer").classList.add("hidden")
}

// info
let infoButtons = [
    document.querySelector("#button-1"),
    document.querySelector("#button-2"),
    document.querySelector("#button-3")
], 
activeSlideId = 1;

function changeInfo(ID){
    let elements = document.getElementsByClassName("slide");
    infoButtons[activeSlideId - 1].classList.remove("active-button");
    infoButtons[ID - 1].classList.add("active-button");

    for (let index = 0; index < elements.length; index++) {
        elements[index].style.transform = `translateX(-${100 * (ID - 1)}%)`;
    }
    activeSlideId = ID;
}

// main slider

let mainID = 0;
function mainSliderPrev(){
    let elements = document.querySelectorAll("#main-img-slide");

    if (mainID <= 0) {
        mainID = elements.length;
    }
    mainID--;
    for (let index = 0; index < elements.length; index++) {
        elements[index].style.transform = `translateX(-${mainID * 100}%)`
    }

}

function mainSliderNext(){
    let elements = document.querySelectorAll("#main-img-slide");

    if (mainID >= elements.length - 1) {
    mainID = -1;
    }
    mainID++;
    for (let index = 0; index < elements.length; index++) {
        elements[index].style.transform = `translateX(-${mainID * 100}%)`
    }
}

// bottom slider
let ID = 0;
function bottomSliderPrev(){
    let elements = document.getElementsByClassName("img-slide");

    if (ID <= 0) {
    ID = elements.length;
    }
    ID--;
    for (let index = 0; index < elements.length; index++) {
        elements[index].style.transform = `translateX(-${ID * 100}%)`
    }

}

function bottomSliderNext(){
  let elements = document.getElementsByClassName("img-slide");

  if (ID >= elements.length - 1) {
        ID = -1;
    }
    ID++;
    for (let index = 0; index < elements.length; index++) {
        elements[index].style.transform = `translateX(-${ID * 100}%)`
    }
}


// FORM
let form = document.querySelector('#offer-form');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    fetch('/send_form/offer', {
        method: 'POST',
        body: new FormData(form)
    })
    .then(response => response.json())
    .then(data => {
        if (data == 200) 
            document.querySelector("#form-send-success").style.display = 'block';
        else 
            document.querySelector("#form-send-error").style.display = 'block';
        submit = document.querySelector("#submit-button");
        submit.disabled = true;
        submit.classList.add('submit-disabled');
    })
    .catch(error => {
        console.error(error);
    })
});