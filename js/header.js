// Define el contenido del encabezado
let headerContenido = `
    <a href=""><img class="logo" src="img/logo.jpg" alt="logo" width="35em" > </a>
    <nav class="navbar-grid"> 
        <ul class="menu">
            <li><a href="index.html" class="item">Inicio</a></li>
            <li><a href="nosotros.html" class="item">Nosotros</a></li>
            <li><a href="galeria.html" class="item">Galeria</a></li>
            <li><a href="contacto.html" class="item">Contacto</a></li>
        </ul> 
    </nav>
`;

// Función para agregar el encabezado a todas las páginas
function agregarHeader() {
    let header = document.createElement('header');
    header.className = 'header-grid';
    header.innerHTML = headerContenido;
    document.body.insertBefore(header, document.body.firstChild);
}

// Llama a la función para agregar el encabezado en cada página
agregarHeader();

    