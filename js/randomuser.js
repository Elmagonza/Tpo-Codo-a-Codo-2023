document.addEventListener("DOMContentLoaded", function () {
    // Espera a que el documento HTML esté completamente cargado antes de ejecutar el código.

    // Obtén referencias a elementos HTML que vamos a utilizar.
    // const userContainer = document.getElementById("userContainer"); // Contenedor principal
    const tituloLiderDelMes = document.getElementById("tituloLiderDelMes"); // Título
    const userImage = document.getElementById("userImage"); // Imagen del usuario
    const userName = document.getElementById("userName"); // Nombre del usuario
    const userEmail = document.getElementById("userEmail"); // Correo electrónico del usuario

    // Función para obtener el nombre del mes actual.
    function getMonthName(month) {
        const monthNames = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
        return monthNames[month];
    }

    // Función para actualizar el título con el mes actual y obtener un usuario.
    function updateTitleAndUser() {
        const today = new Date();
        const currentMonth = today.getMonth(); // Obtiene el mes actual (0-11).
        const currentYear = today.getFullYear(); // Obtiene el año actual.
        const monthName = getMonthName(currentMonth); // Convierte el número del mes en el nombre del mes.
        tituloLiderDelMes.textContent = `Líder del mes de ${monthName} ${currentYear}`; // Actualiza el título con el mes actual.

        // Obtiene el mes almacenado en el almacenamiento local.
        const storedMonth = parseInt(localStorage.getItem("currentMonth"), 10); //el 10 le dice al parseInt que trabajamos con numeros decimales, es decir en base 10

        // Comprueba si el mes ha cambiado o es la primera vez que se carga la página.
        if (isNaN(storedMonth) || storedMonth !== currentMonth) {
            // Si el mes ha cambiado o es la primera vez, obtiene un nuevo usuario aleatorio.
            fetch("https://randomuser.me/api/")
                .then((response) => response.json())
                .then((data) => {
                    const user = data.results[0];
                    localStorage.setItem("currentMonth", currentMonth); // Almacena el mes actual.
                    localStorage.setItem("selectedUser", JSON.stringify(user)); // Almacena los datos del usuario.
                    updateUserData(user); // Actualiza la caja con los datos del nuevo usuario.
                })
                .catch((error) => {
                    console.error("Error al obtener datos del líder:", error);
                });
        } else {
            // Si no ha cambiado el mes, carga el usuario almacenado en el almacenamiento local.
            const user = JSON.parse(localStorage.getItem("selectedUser"));
            updateUserData(user); // Actualiza la caja con los datos del usuario almacenado.
        }
    }

    // Función para actualizar los datos del usuario en la caja.
    function updateUserData(user) {
        const name = `${user.name.first} ${user.name.last}`;
        const email = user.email;
        const picture = user.picture.large;

        userImage.src = picture; // Actualiza la imagen del usuario.
        userName.textContent = name; // Actualiza el nombre del usuario.
        userEmail.textContent = email; // Actualiza el correo electrónico del usuario.
    }

    // Llama a la función para actualizar el título y los datos del usuario al cargar la página.
    updateTitleAndUser();
});
