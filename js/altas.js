const URL = "https://kevingcrimson.pythonanywhere.com/"
// Capturamos el evento de envío del formulario
document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitamos que se envie el form
    var formData = new FormData();
    formData.append('legajo', document.getElementById('legajo').value);
    formData.append('nombre', document.getElementById('nombre').value);
    formData.append('apellido', document.getElementById('apellido').value);
    formData.append('edad', document.getElementById('edad').value);
    formData.append('mail', document.getElementById('mail').value);
    formData.append('rama', document.getElementById('rama').value);
    fetch(URL + 'registros', {
        method: 'POST',
        body: formData // Aquí enviamos formData en lugar de JSON
    })
    .then(function (response) {
        if (response.ok) {
            return response.json();
        }
    })
    .catch(function (error) {
        // Mostramos el error, y no limpiamos el form.
        alert('Error al agregar el registro.');     
        console.error('Error:', error);            
    })
    .finally(function () {
        alert('Registro agregado correctamente.');
        // Limpiar el formulario para el proximo registro
        document.getElementById('legajo').value = "";
        document.getElementById('nombre').value = "";
        document.getElementById('apellido').value = "";
        document.getElementById('edad').value = "";
        document.getElementById('mail').value = "";
        document.getElementById('rama').value = "";
    });
})

