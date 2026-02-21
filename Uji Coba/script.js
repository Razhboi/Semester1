function computeAND() {
    const input1 = document.getElementById("input1").checked;
    const input2 = document.getElementById("input2").checked;
  
    const outputElement = document.getElementById("output");
  
    const result = input1 && input2;
  
    outputElement.innerHTML = `Output: ${result}`;
  }
  