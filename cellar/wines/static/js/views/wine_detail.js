define([
    'jquery',
    'underscore',
    'backbone'
], function($, _, Backbone) {
    var WineView = Backbone.View.extend({

        template:_.template($('#tpl-wine-details').html()),

        render:function (eventName) {
            $(this.el).html(this.template(this.model.toJSON()));
            return this;
        }

    });
    return WineView;
});


