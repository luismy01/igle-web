PersonaDetailView = Backbone.View.extend({

	className: "container-fluid",
	el: $("#el"),

	initialize: function () {
		
		var modal = $('#MyModal');
		var that = this;
		
		modal.on('shown.bs.modal', function (e) {
			modal.find(".btn-modal-eliminar").click(that.Eliminar);
		});
		
	},

	Eliminar: function (e) {
		var deleteUrl = $("#deleteUrl").val();
		window.location = deleteUrl;
	}
    
});

PersonaEditView = Backbone.View.extend({

	className: "container-fluid",
	el: $("#el"),

	initialize: function () {

		var picker = this.$('#fechaNacPicker');
		var that = this;

		picker.datetimepicker({
			format: 'dddd, DD [de] MMMM [de] YYYY',
			date: picker.data("date")
		});

		picker.on("dp.hide", function(e) {
			that.updateDate(e);
		});
		
	},

	updateDate: function (e) {

		var fecha = e.date.format("YYYY-MM-DD");
		this.$("#fecha_nacimiento").val(fecha);
		this.$("#fechaNacimientoInput").val(e.date.format("dddd, DD [de] MMMM [de] YYYY"));
	}

	/*updateTipoIdentificacion: function(evt) {
      
		var $a = $(evt.currentTarget);
		this.$("button.identificacion_descripcion").text($a.text());
		this.$("button.identificacion_descripcion").data("tipo", $a.data("tipo"));

    },*/
    
});
