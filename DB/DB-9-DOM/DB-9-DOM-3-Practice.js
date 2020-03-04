var restart = document.querySelector("#restart");
var cells = document.querySelectorAll("td");

for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener("click", mark)
}

restart.addEventListener("click", function () {
    for (var i = 0; i < cells.length; i++) {
        cells[i].textContent = "";
    }

});

function mark() {
    if (this.textContent == "") {
        this.textContent = "X";
    } else if (this.textContent == "X") {
        this.textContent = "O";
    } else {
        this.textContent = "";
    }
}

