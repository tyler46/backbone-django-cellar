define([
    'underscore',
    'backbone',
    'models/wine'
], function(_, Backbone, Wine) {
    var WineCollection = Backbone.Collection.extend({
        // Reference to this collection's model
        model: Wine,

        url: "/api/v1/wines/",

        parse: function(response) {
            // Response has also meta data for pagination. We want only objects part.
            return response.objects;
        }
    });
    return WineCollection;
});
