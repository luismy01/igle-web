$(function () {
	
	/* inicializa el controlador de la pagina */
	var updateView = new PersonaEditView();

	$("#personaForm").validate({

		errorClass: "has-error",

		errorPlacement: function(error, element) {
			var formGroup = $(element).parents(".form-group");
			formGroup.find(".help-block").text( error.text() );
		},

		highlight: function (element, errorClass, validClass) {
			var formGroup = $(element).parents(".form-group");
			formGroup.addClass(errorClass).removeClass(validClass);
		},

		invalidHandler: function (event, validator) {
			console.log("formulario invalido");
		},

		rules: {

			nombre: {
				required: true
			},

			identificacion_codigo: {
				required: true
			},

			congregacion: {
				required: true
			},

			fechaNacPicker: {
				required: true
			},

			email: {
				email: true,
				required: true
			},

			celular: {
				digits: true,
				required: true
			}

		},

		unhighlight: function (element, errorClass, validClass) {
			var formGroup = $(element).parents(".form-group");
			formGroup.removeClass(errorClass);
			formGroup.find(".help-block").text( "" );
		}

	});
	
});