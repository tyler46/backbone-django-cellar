define([
    'jquery',
    'underscore',
    'backbone'
], function($, _, Backbone) {
    var WineListItemView = Backbone.View.extend({
        tagName:'li',

        template:_.template($('#tpl-wine-list-item').html()),

        render:function (eventName) {
            $(this.el).html(this.template(this.model.toJSON()));
            return this;
        }
    });
    return WineListItemView;
});

