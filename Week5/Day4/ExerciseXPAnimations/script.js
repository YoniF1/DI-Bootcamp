// Part1
// function sayHi(phrase) {
//     alert(phrase);
//   }
  
// setTimeout(sayHi, 2000, "Hello World")

// Part2
// function addParagraph(text) {
//     div = document.getElementById('container')
//     p = document.createElement('p')
//     content = document.createTextNode(text)
//     p.appendChild(content)
//     div.appendChild(p)
// }

// setTimeout(addParagraph, 2000, "Hello World")

// Part3

function addParagraph(text) {
    div = document.getElementById('container')
    p = document.createElement('p')
    content = document.createTextNode(text)
    p.appendChild(content)
    div.appendChild(p)

    number_paras = document.getElementsByTagName('p')
    if(number_paras.length == 5) {
        myStopFunction()
    }
}

timer = setInterval(addParagraph, 2000, "Hello World")

function myStopFunction() {
    clearInterval(timer);
}

// Question3
// button = document.getElementsByTagName('button')[0]
// button.addEventListener('click', myStopFunction)


// Exercise2
// see ex2.js

