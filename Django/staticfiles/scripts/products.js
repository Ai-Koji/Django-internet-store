
// open subcatalogs after click arrow
let active = null;

function openCloseSubdirectories(ID) {
    try {
        if (active != ID )
        closeSubdirectories(active)        
    } catch (error) {
        //
    }

    if (ID == active){
        closeSubdirectories(ID)
    }
    else
        openSubdirectories(ID)
}
 
function closeSubdirectories(ID) {
    active = null

    block = document.querySelector(`#subdirectories-${ID}`)
    block.classList.add('catalog-subdirectories-hidden')
    image = document.querySelector(`#image-${ID}`)
    image.src = '/static/images/arrow-down.svg'
}

function openSubdirectories(ID) {
    active = ID

    block = document.querySelector(`#subdirectories-${ID}`)
    block.classList.remove('catalog-subdirectories-hidden')
    image = document.querySelector(`#image-${ID}`)
    image.src = '/static/images/arrow-up.svg'
}



products = document.querySelectorAll(".page-urls-number").length
if (products > 1) {
    document.querySelector('.page-urls').classList.remove('hidden')
}
