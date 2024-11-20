// Cambia el valor de cada botón de 0 a 1 y viceversa
function toggleValue(id) {
    const button = document.getElementById(id);
    const currentValue = button.textContent.endsWith("0") ? "1" : "0";
    button.textContent = `${button.textContent.slice(0, -1)}${currentValue}`;
}

function simularMultiplexor() {
    const entradas = [
        document.getElementById("D0").textContent.slice(-1),
        document.getElementById("D1").textContent.slice(-1),
        document.getElementById("D2").textContent.slice(-1),
        document.getElementById("D3").textContent.slice(-1),
        document.getElementById("D4").textContent.slice(-1),
        document.getElementById("D5").textContent.slice(-1),
        document.getElementById("D6").textContent.slice(-1),
        document.getElementById("D7").textContent.slice(-1)
    ];

    const inputA = document.getElementById("inputA").textContent.slice(-1);
    const inputB = document.getElementById("inputB").textContent.slice(-1);
    const inputC = document.getElementById("inputC").textContent.slice(-1);
    const outputValue = document.getElementById("outputValue");

    // Convertir las entradas de control a un índice binario
    const binarySelection = inputA + inputB + inputC;
    const selectionIndex = parseInt(binarySelection, 2);

    // Mostrar la salida correspondiente
    outputValue.textContent = `Salida: ${entradas[selectionIndex]}`;
}
