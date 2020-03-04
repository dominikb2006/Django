var playerRed = {
    name: "",
    color: "rgb(255, 0, 0)" //red "Red"//
};
var playerBlue = {
    name: "",
    color: "rgb(0, 0, 255)" //""Blue","Blue"
};
playerBlue.name = prompt("Player One: Enter Your Name, you will be Blue",)
playerRed.name = prompt("Player Two: Enter Your Name, you will be Red",)

var currName = playerBlue.name;
var currColor = playerBlue.color;
var currPlayer = 1;
var table = $("table tr");

// ///
// var rowIndx=1
// var colIndx=1
// var color="Red"
// ///

// $("td").click(function () {
//     var col = $(this).parent().children().index($(this))
//     var row = $(this).parent().parent().children().index($(this).parent())
//     console.log(col);
// });

$("h3").text(playerBlue.name + ": it's your turn, please pick a column to drop your blue chip.");

$("button").on("click", function () {
    var col = $(this).closest("td").index();
    var bottomRow = checkColumn(col);
    console.log(col + "  " + bottomRow);
    setColor(bottomRow, col, currColor);


    if (horizontalCheck() || verticalCheck() || diagonalCheck()) {
        gameEnd(currName);
    }

    currPlayer *= -1;

    if (currPlayer === 1) {
        currName = playerBlue.name;
        $("h3").text(currName + ": it's your turn, please pick a column to drop your blue chip.");
        currColor = playerBlue.color;
    } else {
        currName = playerRed.name;
        $("h3").text(currName + ": it's your turn, please pick a column to drop your red chip.");
        currColor = playerRed.color;
    }

});

function setColor(rowIndx, colIndx, color) {
    return table.eq(rowIndx).find("td").eq(colIndx).find("button").css("background-color", color);
}

function getColor(rowIndx, colIndx) {
    return table.eq(rowIndx).find("td").eq(colIndx).find("button").css("background-color");
}

function checkColumn(colIndx) {
    for (var i = 5; i > -1; i--) {
        if (getColor(i, colIndx) === "rgb(128, 128, 128)") {
            return i;
        }
    }
}

function colorCheck(one, two, three, four) {
    return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

function horizontalCheck() {
    for (var row = 0; row < 6; row++) {
        for (var col = 0; col < 4; col++) {
            if (colorCheck(getColor(row, col), getColor(row, col + 1), getColor(row, col + 2), getColor(row, col + 3))) {
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

function verticalCheck() {
    for (var row = 0; row < 7; row++) {
        for (var col = 0; col < 3; col++) {
            if (colorCheck(getColor(row, col), getColor(row + 1, col), getColor(row + 2, col), getColor(row + 3, col))) {
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

function diagonalCheck() {
    for (var col = 0; col < 5; col++) {
        for (var row = 0; row < 7; row++) {
            if (colorCheck(getColor(row, col), getColor(row + 1, col + 1), getColor(row + 2, col + 2), getColor(row + 3, col + 3))) {
                console.log('diag');
                reportWin(row, col);
                return true;
            } else if (colorCheck(getColor(row, col), getColor(row - 1, col + 1), getColor(row - 2, col + 2), getColor(row - 3, col + 3))) {
                console.log('diag');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

function reportWin(row, col) {
    console.log("You won game starting at this row, col");
    console.log(row + ", " + col)
}

function gameEnd(winningPlayer) {
    for (var col = 0; col < 7; col++) {
        for (var row = 0; row < 7; row++) {
            $("h3").fadeOut("fast");
            $("h2").fadeOut("fast");
            $("h1").text(winningPlayer + " has won! Refresh your browser to play again!").css("fontSize", "50px")
        }
    }
}

// function setColor() {
//     for (i = 0; i < 7; i++) {
//         if ($(this).css("background-color") !== "rgb(255, 0, 0)" && $(this).css("background-color") !== "rgb(0, 0, 255)") { //do zmiany
//             if (countClick % 2 === 0) {
//                 color = playerBlue.color;
//                 // col = $("td").parent().children().index($("td"));
//                 $("h3").text(playerRed.name + ": it"s your turn, please pick a column to drop your red chip");
//
//             } else if (countClick % 2 === 1) {
//                 color = playerRed.color;
//                 // col = $("td").parent().children().index($("td"));
//                 $("h3").text(playerBlue.name + ": it"s your turn, please pick a column to drop your blue chip");
//             }
//             console.log(col);
//             $(this).css("background-color", color);
//             // $(this).text(col);
//             countClick += 1;
//             console.log(countClick)
//         }
//     }
// }

function getIndex() {
    var col = $(this).index();
    var row = $(this).closest("tr").index();

}