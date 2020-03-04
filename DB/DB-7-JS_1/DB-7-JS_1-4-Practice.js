var fname;
var lname;
var age;
var tall;
var pname;

fname = prompt("Hello and Welcome. Please enter your First Name:");
lname = prompt("Please enter your last Name:");
age = prompt("How old are you?");
tall = prompt("How tall are you in centimeters?");
pname = prompt("What is the name of your pet?");
alert("Thank you so much for the information.");

if ((fname[0].toLowerCase() == lname[0].toLowerCase()) && (age >= 20 && age <= 30) && (tall >= 170) && (pname[pname.length-1] == "y")) {

    console.log("Welcome Comrade! you've passed the Spy Test");

} else {

    console.log("Sorry, nothing to see here.");
}




