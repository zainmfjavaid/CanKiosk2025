var timestamp = Date.now();
var checkTime = null;

var timeoutDuration = 130000;

document.addEventListener('DOMContentLoaded', function(){
    checkTime = setInterval(doTimeout, timeoutDuration);
});


document.addEventListener("click", function() {
    console.log("Click");
    timestamp = Date.now();
});

document.addEventListener("scroll", function() {
    console.log("Scroll");
    timestamp = Date.now();
});

function doTimeout(){
    if (Date.now() - timestamp >= timeoutDuration){
        window.location.href = "/"
    }
}