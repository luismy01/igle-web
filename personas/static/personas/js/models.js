PersonaModel = Backbone.Model.extend({
	
	urlRoot: "/personas/",

	defaults: {
		nombre: '',
		identificacion_tipo: 'CC', // CC, TI, PS
		identificacion_descripcion: 'Cédula de ciudadanía',
		identificacion_codigo: '',
		congregacion: '',
		fecha_nacimiento: null,
		email: '',
		celular: '',
		genero: 'M', // M, F
		habilitado: true, // true, false
	},
	
	initialize: function() {
		this.on("change", this.updateIdentificacion);
		//this.updateIdentificacion();
	},

	/*updateIdentificacion: function() {

		if ( this.get('identificacion_tipo') === 'CC' ) {
			this.set("identificacion_descripcion", 'Cédula de ciudadanía');
		
		} else if ( this.get('identificacion_tipo') === 'TI' ) {
			this.set("identificacion_descripcion", 'Tarjeta de identidad');

		} else if ( this.get('identificacion_tipo') === 'PS' ) {
			this.set("identificacion_descripcion", 'Pasaporte');

		}

	}*/

});