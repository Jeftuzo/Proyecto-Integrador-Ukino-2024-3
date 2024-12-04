// Cambia el valor de cada botón entre 0 y 1
function toggleValue(id) {
    const button = document.getElementById(id);
    const currentValue = button.textContent.endsWith("0") ? "1" : "0";
    button.textContent = `${button.textContent.slice(0, -1)}${currentValue}`;
}

function simularDemux() {
    const input = document.getElementById("X").textContent.slice(-1);
    const inputA = document.getElementById("inputA").textContent.slice(-1);
    const inputB = document.getElementById("inputB").textContent.slice(-1);
    const inputC = document.getElementById("inputC").textContent.slice(-1);

    const binarySelection = inputA + inputB + inputC;
    const selectionIndex = parseInt(binarySelection, 2);

    const outputs = document.getElementById("outputs").children;

    // Reiniciar todas las salidas a 0
    for (let i = 0; i < outputs.length; i++) {
        outputs[i].textContent = `Y${i}: 0`;
    }

    // Asignar el valor de la entrada a la salida seleccionada
    outputs[selectionIndex].textContent = `Y${selectionIndex}: ${input}`;
}
