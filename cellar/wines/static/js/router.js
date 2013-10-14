define([
    'jquery', 
    'underscore',
    'backbone',
    'collections/wines',
    'models/wine',
    'views/wine_list',
    'views/wine_detail'
], function($, _, Backbone, WineCollection, Wine, WineListView, WineView) {
    var AppRouter = Backbone.Router.extend({
        
        routes: {
            "":"list",
            "wines/:id":"wineDetails"
        },

        list:function () {
            this.wineList = new WineCollection();
            this.wineListView = new WineListView({model:this.wineList});
            this.wineList.fetch();
            $('#sidebar').html(this.wineListView.render().el);
        },

        wineDetails:function (id) {
            this.wine = this.wineList.get(id);
            this.wineView = new WineView({model:this.wine});
            $('#content').html(this.wineView.render().el);
        }
    });

    return AppRouter;
});
