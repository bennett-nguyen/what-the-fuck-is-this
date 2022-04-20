let displayer = document.getElementById("expression");
let float = document.getElementById('float');
var preFloat = '...';
var preTotal = '';

const button1 = document.getElementById('b1');
const button2 = document.getElementById('b2');
const button3 = document.getElementById('b3');
const button4 = document.getElementById('b4');
const button5 = document.getElementById('b5');
const button6 = document.getElementById('b6');
const button7 = document.getElementById('b7');
const button8 = document.getElementById('b8');
const button9 = document.getElementById('b9');
const button0 = document.getElementById('b0');

const addButton = document.getElementById('bp');
const subButton = document.getElementById('bm');
const mulButton = document.getElementById('bmu');
const divButton = document.getElementById('bd');
const perButton = document.getElementById('PERIOD');
const ClrButton = document.getElementById('CLEAR');
const evaluate = document.getElementById('eval');
const openParent = document.getElementById('openParent');
const closeParent = document.getElementById("closeParent");
const SingleClr = document.getElementById('ACLEAR');


let expression = '0';






// For Buttons


// numbers
button1.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '1';
    displayer.innerHTML = expression;
    
})

button2.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '2';
    displayer.innerHTML = expression;
})

button3.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '3';
    displayer.innerHTML = expression;
})

button4.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '4';
    displayer.innerHTML = expression;
})

button5.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '5';
    displayer.innerHTML = expression;
})

button6.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '6';
    displayer.innerHTML = expression;
})

button7.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '7';
    displayer.innerHTML = expression;
})

button8.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '8';
    displayer.innerHTML = expression;
})

button9.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '9';
    displayer.innerHTML = expression;
})

button0.addEventListener("click", () => {
    float.innerHTML = preFloat;
    if (expression === '0') {
        expression = ''
    }
    expression = expression + '0';
    displayer.innerHTML = expression;
})


// operators
addButton.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + '+';
    displayer.innerHTML = expression;
})

subButton.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + '-';
    displayer.innerHTML = expression;
})

mulButton.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + '*';
    displayer.innerHTML = expression;
})

divButton.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + '/';
    displayer.innerHTML = expression;
})

perButton.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + '.';
    displayer.innerHTML = expression;
})

openParent.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + '(';
    displayer.innerHTML = expression;
})

closeParent.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = expression + ')';
    displayer.innerHTML = expression;
})


// function buttons
SingleClr.addEventListener('click', () => {
    expression = expression.slice(0, -1)
    
    if (!expression.length) {
        displayer.innerHTML = '0' 
    } else {
        displayer.innerHTML = expression;
    }
})

evaluate.addEventListener('click', () => {
    try {
        const total = eval(expression).toString();
        let result = `${expression} = ${total}`

        if (total === "Infinity" || total === "NaN" || total === "undefined") {
            displayer.innerHTML = 'ERROR';
            expression = ''
        } else {
            preTotal = total;
            if (result.length > 30) {
                preFloat = `${total.substr(0, 40)}...`
                float.innerHTML = `${expression.substr(0, 30)}... =`
                displayer.innerHTML = total
            } else {
                float.innerHTML = `${expression} =`;
                preFloat = result;
            }


            displayer.innerHTML = total;

            expression = '0'
        }
    } catch (err) {
        displayer.innerHTML = 'ERROR';
        expression = ''
    }
})

ClrButton.addEventListener('click', () => {
    float.innerHTML = preFloat;
    expression = '0';
    displayer.innerHTML = expression;
})


// For Keys

document.addEventListener('keydown', (event) => {
    if (!event.shiftKey) {
        switch (event.keyCode) {

            // numbers
            case 48:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '0';
                displayer.innerHTML = expression;
                break;

            case 49:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '1';
                displayer.innerHTML = expression;
                break;

            case 50:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '2';
                displayer.innerHTML = expression;
                break;

            case 51:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '3';
                displayer.innerHTML = expression;
                break;

            case 52:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '4';
                displayer.innerHTML = expression;
                break;

            case 53:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '5';
                displayer.innerHTML = expression;
                break;

            case 54:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '6';
                displayer.innerHTML = expression;
                break;
                
            case 55:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '7';
                displayer.innerHTML = expression;
                break;

            case 56:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '8';
                displayer.innerHTML = expression;
                break;

            case 57:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + '9';
                displayer.innerHTML = expression;
                break;

            // operators
            case 189:
                float.innerHTML = preFloat;
                expression = expression + '-';
                displayer.innerHTML = expression;
                break;

            case 191:
                float.innerHTML = preFloat;
                expression = expression + '/';
                displayer.innerHTML = expression;
                break;

            case 190:
                float.innerHTML = preFloat;
                expression = expression + '.';
                displayer.innerHTML = expression;
                break;
            //

            case 13:  // eval
                try {
                    const total = eval(expression).toString();
                    let result = `${expression} = ${total}`

                    if (total === "Infinity" || total === "NaN" || total === "undefined") {
                        displayer.innerHTML = 'ERROR';
                        expression = ''
                    } else {
                        preTotal = total;
                        if (result.length > 30) {
                            preFloat = `${total.substr(0, 40)}...`;
                            float.innerHTML = `${expression.substr(0, 30)}... =`;
                            displayer.innerHTML = total;
                        } else {
                            float.innerHTML = `${expression} =`;
                            preFloat = result;
                            
                        }

                        displayer.innerHTML = total;


                        expression = '0';
                    }
                } catch(err) {
                    displayer.innerHTML = 'ERROR';
                    expression = '';
                }
                break;

            case 8: // clear all
                float.innerHTML = preFloat;
                expression = '0';
                displayer.innerHTML = expression;
                break;

            case 37: // single clear
                float.innerHTML = preFloat;
                expression = expression.slice(0, -1)
                if (!expression.length) {
                    displayer.innerHTML = '0';
                } else {
                    displayer.innerHTML = expression;
                }
                break;
            
        }
    }

    // operators
    else if (event.shiftKey){
        switch(event.keyCode) {
            case 187:
                float.innerHTML = preFloat;
                expression = expression + '+';
                displayer.innerHTML = expression;
                break;

            case 56:
                float.innerHTML = preFloat;
                expression = expression + '*';
                displayer.innerHTML = expression;
                break;
            
            case 57:
                float.innerHTML = preFloat;
                expression = expression + '(';
                displayer.innerHTML = expression;
                break;

            case 48:
                float.innerHTML = preFloat;
                expression = expression + ')';
                displayer.innerHTML = expression;
                break;
            //

            case 81:
                float.innerHTML = preFloat;
                if (expression === '0') {
                    expression = '';
                }
                expression = expression + preTotal;
                displayer.innerHTML = expression;
                break;
        }
    }
})