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

let footerContenido = `
 <div>
    <h4>Grupo Scout Nº7-Sagrado Corazón </h4>
    <br>
    <p>&copy; 2023-Desarrollado por alumnos de Codo a Codo </p>
</div>
<div>
    <h4>Contacto</h4>
    <ul>
    <li>Tel:xx xxxx-xxxx</li>
    <li>Dirección:Av. Gral. Tomás de Iriarte 3051</li>
    <li>Gmail:xxxxxxx@gmail.com</li>
    </ul>
</div>
<div class="redes">  <h4>Nuestras redes</h4>
    <a href="https://www.facebook.com/sagradocorazonbarracas" target="_blank"><img src="img/redes/facebook.png"
            alt="Facebook" width="20em" title="Ir a Facebook"></a>
    <a href="https://www.instagram.com/scoutsagrado/" target="_blank"><img src="img/redes/instagram.png"
            alt="Instagram" width="20em" title="Ir a Instagram"></a>
    <a href="https://twitter.com/ScoutsSagrado" target="_blank"><img src="img/redes/twitter.png" alt=""
            width="20em" title="Ir a Twitter"></a>
</div>
`;

// Función para agregar el footer a todas las páginas
function agregarFooter() {
    let footer = document.createElement('footer');
    footer.id = "footer";
    footer.className = 'footer';
    footer.innerHTML = footerContenido;
    document.body.appendChild(footer);
}
    
agregarFooter();
