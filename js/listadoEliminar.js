const URL = "http://127.0.0.1:5000/"
const app = Vue.createApp({
    data() {
        return {
            registros: []
        }
    },
    methods: {
        obtenerRegistros() {
        // Obtenemos el contenido de la nómina
            fetch(URL + 'registros')
                .then(response => {
                // Parseamos la respuesta JSON
                    if (response.ok) { return response.json(); }})
                .then(data => {
                // El código Vue itera este elemento para generar la tabla
                    this.registros = data;})
                .catch(error => {
                    console.log('Error:', error);
                    alert('Error al obtener los registros.');
                });
        },
        eliminarRegistro(legajo) {
            if (confirm('¿Estás seguro de que quieres eliminar este registro?')) {

                fetch(URL + `registros/${legajo}`, { method: 'DELETE' })
                    .then(response => {
                        if (response.ok) {
                            this.registros = this.registros.filter(registro => registro.legajo !== legajo);
                            alert('Registro eliminado correctamente.');
                        }}
                    )
                    .catch(error => {
                        alert(error.message);
                    });
            }
        }
    },
    mounted() {
        //Al cargar la página, obtenemos la lista de registros
        this.obtenerRegistros();
    }
});
app.mount('body');