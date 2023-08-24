products = document.querySelectorAll(".page-urls-number").length
console.log(products)
if (products > 1) {
    document.querySelector('.page-urls').classList.remove('hidden')
}
