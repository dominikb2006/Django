// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = [];

// Create the functions for the tasks
let start;
var choose;
var name;
start = prompt("Would you like to start the roster web app? y/n");

while (start === "y") {
    choose = prompt("Please select an action: add, remove, display, or quit.");
    if (choose == "add") {
        name = prompt("What name would you like to add?");
        addNew(roster, name);
    } else if (choose == "remove") {
        rmv(roster);
    } else if (choose == "display") {
        display(roster);
    } else if (choose == "quit") {
        start = "n"
    }
}

// ADD A NEW STUDENT
function addNew(arr, name) {
    arr.push(name);
}

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

// REMOVE STUDENT
function rmv(arr) {
    arr.splice(arr.length - 1, 1);
}

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
// DISPLAY ROSTER
function display(arr) {
    console.log(arr);
}

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
