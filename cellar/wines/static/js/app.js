require.config({
    baseUrl: "/static/js/",
    /* 
        Underscore and Backbone are not compatible with AMD.
    */
    shim: {
        'underscore': {
            exports: "_"
        },
        'backbone': {
            deps: ["underscore", "jquery"],
            exports: "Backbone"
        }
    },
    paths: {
        underscore: "lib/underscore",
        jquery: "lib/jquery-1.7.1.min",
        backbone: "lib/backbone",
    }
});


require([
    "jquery",
    "underscore",
    "backbone",
    "router"
], function($, _, Backbone, AppRouter) {
    return $(document).ready(function() {
        var router;
        router = new AppRouter();
        return Backbone.history.start();
    });
});

