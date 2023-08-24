// slider
let currentSlide = 0,
    slides = document.querySelectorAll(".slide"),
    buttons = document.querySelectorAll('.slide-button'),
    arrows = document.querySelectorAll('.arrow'),
    autoSlideInterval;

// Function to change slide
function changeSlide() {
    for (let index = 0; index < slides.length; index++) {
        slides[index].style.transform = `translateX(-${100 * currentSlide}%)`;
    }
    buttons.forEach(button => button.classList.remove("active-button"));
    buttons[currentSlide].classList.add("active-button");
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    changeSlide();
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    changeSlide();
}

function goToSlide(slideIndex) {
    currentSlide = slideIndex;
    changeSlide();
}

// Add event listeners
arrows.forEach(arrow => arrow.addEventListener('click', event => {
    if (event.currentTarget.classList.contains('arrow-left')) {
        prevSlide();
    } else if (event.currentTarget.classList.contains('arrow-right')) {
        nextSlide();
    }
    stopAutoSlide(); // Остановить автосмену слайдов при нажатии на стрелку
}));

buttons.forEach((button, index) => button.addEventListener('click', () => {
    goToSlide(index);
    stopAutoSlide(); // Остановить автосмену слайдов при нажатии на кнопку
}));

function startAutoSlide() {
    autoSlideInterval = setInterval(nextSlide, 5000);
}

function stopAutoSlide() {
    clearInterval(autoSlideInterval);
}

startAutoSlide(); // Начать автосмену слайдов
