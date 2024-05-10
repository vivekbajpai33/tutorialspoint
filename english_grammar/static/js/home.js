// owl carousel js

$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            600: {
                items: 3,
                nav: false
            },
            1000: {
                items: 5,
                nav: true,
                loop: false
            }
        }
    })
});

// pop up form

let popup = document.getElementById("pop_up");
function OpenPopUp() {
    popup.classList.add("open-popup")
}

function ClosePopUp() {
    popup.classList.remove("open-popup")
}


