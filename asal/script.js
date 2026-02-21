function validateInputA() {
    var inputA = document.getElementById("inputA");
    var validationMessage = document.getElementById("validationMessage");

    if (inputA.value < 0 || inputA.value > 1) {
    validationMessage.innerHTML = "Harap masukkan nilai antara 0 dan 1.";
    inputA.setCustomValidity("Invalid input");
    } else {
    validationMessage.innerHTML = "";
    inputA.setCustomValidity("");
    }
}





// Function to perform AND operation
function performAND() {
    let inputA = document.getElementById('inputA').value === '1';
    let inputB = document.getElementById('inputB').value === '1';
    let result = inputA && inputB;

    // Display the result
    document.getElementById('resultAND').innerText = `Result of AND operation: ${result ? 'True' : 'False'}`;
}

// Function to perform OR operation
function performOR() {
    let inputA = document.getElementById('inputA').value === '1';
    let inputB = document.getElementById('inputB').value === '1';
    let result = inputA || inputB;

    // Display the result
    document.getElementById('resultOR').innerText = `Result of OR operation: ${result ? 'True' : 'False'}`;
}

// Function to perform NOT operation
function performNOT() {
    let inputA = document.getElementById('inputA').value === '1';
    let result = !inputA;

    // Display the result
    document.getElementById('resultNOT').innerText = `Result of NOT operation: ${result ? 'True' : 'False'}`;
}

// Function to perform XOR operation
function performXOR() {
    let inputA = document.getElementById('inputA').value === '1';
    let inputB = document.getElementById('inputB').value === '1';
    let result = (inputA || inputB) && !(inputA && inputB);

    // Display the result
    document.getElementById('resultXOR').innerText = `Result of XOR operation: ${result ? 'True' : 'False'}`;
}

// Function to perform XNOR operation
function performXNOR() {
    let inputA = document.getElementById('inputA').value === '1';
    let inputB = document.getElementById('inputB').value === '1';
    let result = !(inputA || inputB) || (inputA && inputB);

    // Display the result
    document.getElementById('resultXNOR').innerText = `Result of XNOR operation: ${result ? 'True' : 'False'}`;
}

// Function to perform NOR operation
function performNOR() {
    let inputA = document.getElementById('inputA').value === '1';
    let inputB = document.getElementById('inputB').value === '1';
    let result = !(inputA || inputB);

    // Display the result
    document.getElementById('resultNOR').innerText = `Result of NOR operation: ${result ? 'True' : 'False'}`;
}

// Function to perform NAND operation
function performNAND() {
    let inputA = document.getElementById('inputA').value === '1';
    let inputB = document.getElementById('inputB').value === '1';
    let result = !(inputA && inputB);

    // Display the result
    document.getElementById('resultNAND').innerText = `Result of NAND operation: ${result ? 'True' : 'False'}`;
}
