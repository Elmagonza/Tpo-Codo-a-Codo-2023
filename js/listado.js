const URL = "http://127.0.0.1:5000/"
// Realizamos la solicitud GET al servidor para obtener todos los registros
fetch(URL + '/registros')
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            // Si hubo un error, lanzar explícitamente una excepción
            // para ser "catcheada" más adelante
            throw new Error('Error al obtener los registros.');
        }
    })
    .then(function (data) {
        let tablaregistros = document.getElementById('tabla-registros');
        // Iteramos sobre los registros y agregamos filas a la tabla
        for (let registro of data) {
            let fila = document.createElement('tr');
            fila.innerHTML = '<td>' + registro.legajo + '</td>' +'<td>' + registro.nombre + '</td>' +'<td >' + registro.apellido + '</td>' +'<td>' + registro.edad + '</td>' +'<td>' + registro.mail + '</td>' + '<td>' + registro.rama + '</td>';
        //Una vez que se crea la fila con el contenido del registro,se agrega a la tabla utilizando el método appendChild del elementotablaregistros.
        tablaregistros.appendChild(fila);
        }
    })
    .catch(function (error) {
    // En caso de error
    alert('Error al agregar el registro.');
    console.error('Error:', error);
    })