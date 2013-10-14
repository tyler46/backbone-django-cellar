define([
    'jquery',
    'underscore',
    'backbone',
    'views/wine_list_item'
], function($, _, Backbone, WineListItemView) {
    
    var WineListView = Backbone.View.extend({
        tagName:'ul',

        initialize:function () {
            this.model.bind('reset', this.render, this);
        },

        render:function (eventName) {
            _.each(this.model.models, function (wine) {
                $(this.el).append(new WineListItemView({model: wine}).render().el);
            }, this);
            return this;
        }
    });
    return WineListView;

});
