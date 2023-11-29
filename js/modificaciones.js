const URL = "http://127.0.0.1:5000/"
const app = Vue.createApp({
    data() {
        return {
            legajo: '',
            nombre: '',
            apellido: '',
            edad: '',
            mail: '',
            rama: '',
            mostrarDatosregistro: false,
        };
    },
    methods: {
        obtenerRegistro() {
            fetch(URL + '/registros/' + this.legajo)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
//Si la respuesta es un error, lanzamos una excepción para ser "catcheada" más adelante en el catch.

                        throw new Error('Error al obtener los datos del registro.')

                    }
                })
                .then(data => {
                    this.nombre = data.nombre;
                    this.apellido = data.apellido;
                    this.edad = data.edad;
                    this.mail = data.mail;
                    this.rama= data.rama;
                    this.mostrarDatosregistro = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('Legajo no encontrado.');
                })
        },
        guardarCambios() {
            const formData = new FormData();
            formData.append('legajo', this.legajo);
            formData.append('nombre', this.nombre);
            formData.append('apellido', this.apellido);
            formData.append('edad', this.edad);
            formData.append('mail', this.mail); 
            formData.append('rama', this.rama); 
            //Utilizamos fetch para realizar una solicitud PUT a la API y guardar los cambios.
            
            fetch(URL + '/registros/' + this.legajo, {
                method: 'PUT',
                body: formData,
            })
            .then(response => {
            //Si la respuesta es exitosa, utilizamos response.json()para parsear la respuesta en formato JSON.
                if (response.ok) {
                    return response.json()
                } else {
            //Si la respuesta es un error, lanzamos una excepción.
            
                    throw new Error('Error al guardar los cambios del registro.')
            }
            })
            .then(data => {
                alert('registro actualizado correctamente.');
                this.limpiarFormulario();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el registro.');
            });
            },
            limpiarFormulario() {
                this.legajo = '';
                this.nombre = '';
                this.apellido = '';
                this.edad = '';
                this.mail = '';
                this.rama = '';
                this.mostrarDatosregistro = false;
            }
            }
            });
app.mount('#app');