// Define el contenido del encabezado
let headerContenido = `
    <a href=""><img class="logo" src="img/logo.png" alt="logo" width="35em" > </a>
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

let footerContenido = `

    <div class="box">
        <div class="esc">
            <h1>Grupo Scout Nº7-Sagrado Corazón </h1>
        </div>
    </div>
    <div class="box">
        <h2>Nuestras redes</h2>
        <div class="redes-soc">
            <a href="https://www.facebook.com/sagradocorazonbarracas" target="_blank"><img
                    src="img/redes/facebook.png" alt="Facebook" width="20em" title="Ir a Facebook"></a>
            <a href="https://www.instagram.com/scoutsagrado/" target="_blank"><img src="img/redes/instagram.png"
                    alt="Instagram" width="20em" title="Ir a Instagram"></a>
            <a href="https://twitter.com/ScoutsSagrado" target="_blank"><img src="img/redes/twitter.png" alt=""
                    width="20em" title="Ir a Twitter"></a>
        </div>
    </div>
    <div class="grupo2">
        <p>&copy; Derechos reservados 2023<br>Desarrollado por alumnos de Codo a Codo </p>
    </div>

`;

// Función para agregar el footer a todas las páginas
function agregarFooter() {
    let footer = document.createElement('footer');
    footer.id = "pie";
    footer.className = 'footer';
    footer.innerHTML = footerContenido;
    document.body.appendChild(footer);
}

agregarFooter();
