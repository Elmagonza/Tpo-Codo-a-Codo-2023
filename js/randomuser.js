document.addEventListener("DOMContentLoaded", function () {
    const userContainer = document.getElementById("userContainer");
    const tituloLiderDelMes = document.getElementById("tituloLiderDelMes");
    const userData = document.getElementById("userData");
    const userImage = document.getElementById("userImage");
    const userName = document.getElementById("userName");
    const userEmail = document.getElementById("userEmail");

    // Función para obtener el nombre del mes actual
    function getMonthName(month) {
        const monthNames = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
        return monthNames[month];
    }

    // Función para actualizar el título con el mes actual
    function updateTitleWithCurrentMonth() {
        const today = new Date();
        const currentMonth = today.getMonth(); //devuelve el mes en numero de 1 a 12
        const currentYear = today.getFullYear(); 
        const monthName = getMonthName(currentMonth);
        tituloLiderDelMes.textContent = `Líder del mes de ${monthName} ${currentYear}`;
    }

    // Llama a la función para actualizar el título con el mes actual
    updateTitleWithCurrentMonth();

    // Función para obtener un usuario aleatorio desde la API de RandomUser y mostrarlo
    function getRandomUserAndDisplay() {
        // Comprobar si ya hay un usuario almacenado en el almacenamiento local
        const storedUser = localStorage.getItem("selectedUser");

        if (storedUser) {
            // Si hay un usuario almacenado, mostrarlo en lugar de obtener uno nuevo
            const user = JSON.parse(storedUser);
            updateUserData(user);
        } else {
            // Si no hay un usuario almacenado, obtener uno nuevo
            fetch("https://randomuser.me/api/")
                .then((response) => response.json())
                .then((data) => {
                    const user = data.results[0];
                    updateUserData(user);
                    // Almacenar el usuario en el almacenamiento local
                    localStorage.setItem("selectedUser", JSON.stringify(user));
                })
                .catch((error) => {
                    console.error("Error al obtener datos del líder:", error);
                });
        }
    }

    // Función para actualizar los datos del usuario en la caja
    function updateUserData(user) {
        const name = user.name.first + " " + user.name.last;
        const email = user.email;
        const picture = user.picture.large;

        userImage.src = picture;
        userName.textContent =  `${name}`;
        userEmail.textContent = `${email}`;
    }

    // Llama a la función para obtener y mostrar el usuario aleatorio al cargar la página
    getRandomUserAndDisplay();
});
