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
    
});

PersonaListItemView = Backbone.View.extend({

    className: "col-lg-3 col-md-4 col-sm-4 col-xs-12 portfolio-item",
    tagName: "div",
    template_name: "#PersonaListItemView",
        
    render: function () {
        
        var engine = _.template( $(this.template_name).html() );
        var html = engine({p: this.model});
        
        this.$el.html(html);
        
        var a = $(".detail-link", this.el);
        var href = a.attr("href");
		
        a.attr("href", href.replace("0", this.model.get('id')));
		
    }

});

PersonaListView = Backbone.View.extend({
	
	el: "#listView",

	events: {
		"click #btnBuscar": "buscar",
		"click #btnAgregarPersona": "agregarPersona"
	},
    
	agregarPersona: function (e) {},
	
	buscar: function (e) {
		
		var query = this.clean_text(this.$("#txtBuscar").val());
		var that = this;
				
		var models = this.collection.filter(function (p){
			var nombre = that.clean_text(p.get("nombre"));
			return (nombre.indexOf(query) >= 0);
		});
		
		this.render({collection: new PersonaCollection(models)});
		
	},
	
	clean_text: function (text) {
		text = text.toLowerCase();
		return text;
	},
	
	render: function(options) {
        
		var collection;
		var view = this;
		
		options = options || {};
		
        if (options.collection != undefined) {
			collection = options.collection;
		} else {
			collection = this.collection;
		}
		
		var $persona_list = $("#persona-list", view.el);
		
		view.trigger("render");
		$persona_list.html('');
		
		collection.each( function (persona) {
            
			var listViewItem = new PersonaListItemView({model: persona});
			listViewItem.listenTo(view, "render", listViewItem.remove);
			listViewItem.render();
			
			$(listViewItem.el).hide()
				.appendTo($persona_list)
				.fadeIn( "slow" );

		});
		
    },
    
});
