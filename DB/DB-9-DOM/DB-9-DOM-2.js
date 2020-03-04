var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener("mouseover", function () {
    headOne.textContent = "Mouse Currently Over";
    headOne.style.color = "red";
});

headOne.addEventListener("mouseout", function () {
    headOne.textContent = "Hover OVER ME!";
    headOne.style.color = "black";
});

headTwo.addEventListener("click", function () {
    headTwo.textContent = "YOU CLICKED ME BASTERD!";
    headTwo.style.color = "blue";
});

headThree.addEventListener("dblclick", function () {
    headThree.textContent = "YOU DOUBLE CLICKED ME BASTERD!";
    headThree.style.color = "green";
});