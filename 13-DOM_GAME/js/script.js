//Restart Game button
//#b is id of restart button
var restart = document.querySelector("#b");
//Grabs all the squares
//select all td
var squares = document.querySelectorAll('td');
//Clear all the squares
//clear td in table
function clearBoard(){
    for(var i = 0; squares.length;i++){
        squares[i].textContent = '';
    }
}

restart.addEventListener('click',clearBoard);
//Check the square marker

//Example
// var cellOne = document.querySelector('#one');
// cellOne.addEventListener('click',function(){
//     cellOne.textContent = 'X';
//     if (cellOne.textContent === ''){
//         cellOne.textContent = 'X';
//     } else if (cellOne.textContent === 'X') {
//         cellOne.textContent = 'O';
//     } else {
//         cellOne.tagContent = '';
//     }
// })

function changeMarker(){
    if (this.textContent === ''){
        this.textContent = 'X';
    } else if (this.textContent === 'X') {
        this.textContent = 'O';
    } else {
        this.textContent = '';
    }
}

for (var i = 0 ; i < squares.length; i++) {
    squares[i].addEventListener('click',changeMarker);
}

//For loop to add event listeners to all the squares