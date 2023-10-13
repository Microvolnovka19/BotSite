clck = document.getElementById("clock_text")
tt = document.getElementById("daynight")

rndtxt = document.getElementById("random_text")
toggle = document.getElementById("toggle2")
once = true

facttext = document.getElementById("fact_text")

song = document.getElementById("test_song")
song_time = document.getElementById("song_time")

function myClock() {
    var today = new Date()
    currnum = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    clck.textContent = currnum

    if (once){
        once = false

        if (today.getHours() <= 6 || today.getHours() >= 22){
            tt.textContent = "Ночь ёпта"
        }
        else if (today.getHours() > 6 || today.getHours() <= 10){
            tt.textContent = "Утро ёпта"
        }
        else if (today.getHours() > 10|| today.getHours() <= 18){
            tt.textContent = "День ёпта"
        }
        else if (today.getHours() > 18 || today.getHours() < 22){
            tt.textContent = "Вечер ёпта"
        }
        else {
            tt.textContent = "Чо за хуйня"
        }

        }
    }

function makeid() {
        if (toggle.checked){
        let result = '';
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
        const charactersLength = characters.length;
        let counter = 0;
        while (counter < 20) {
          result += characters.charAt(Math.floor(Math.random() * charactersLength));
          counter += 1;
        }
        rndtxt.textContent = result;
    }
}
    

setInterval(makeid,250)

setInterval(myClock,1000)

function makefact(){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "https://catfact.ninja/fact");
    xhr.send();
    xhr.responseType = "json";
    xhr.onload = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {

        
        facttext.textContent = xhr.response.fact


    } else {
        console.log(`Error: ${xhr.status}`);
    }
    };
}

console.log(test_song)
test_song.volume = 0.05

function updateSongTime() {
    if(!test_song.paused){
        song_time.textContent = Math.round(test_song.currentTime) + " / " + Math.round(test_song.duration)
    }
}
function startsong(){
    test_song.play()
    console.log(test_song.startDate)
}
function pausesong(){
    test_song.pause()
}

setInterval(updateSongTime,1000)