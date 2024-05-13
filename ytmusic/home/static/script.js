var play = document.getElementById("play");
var audio = document.getElementById("audio");
function togglePlay() {
    if (audio.paused) {
      audio.play();
      play.classList.add("pause");
    } else {
      audio.pause();
      play.classList.remove("pause");
    }
}

play.addEventListener("click", togglePlay);