window.onload = init;

function init(){
    var rests = document.querySelector('#rests')
    var delete = function(e){
        alert(e.target + ' ' + e.currentTarget);
    };
    rests.addEventListener("click", delete, false)
}