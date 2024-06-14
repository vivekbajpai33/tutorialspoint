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


document.addEventListener('DOMContentLoaded', function() {
    var toasts = document.querySelectorAll('.toast');
    toasts.forEach(function(toast) {
        setTimeout(function() {
            toast.classList.add('toast-show');
        }, 100); // slight delay to trigger the animation

        setTimeout(function() {
            toast.classList.remove('toast-show');
            toast.classList.add('toast-hide');
        }, 10000); // hide after 10 seconds
    });
});

