requirejs.config({
    paths: {
        jquery: [
            'https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min',
            'jquery-1.10.2.min'
        ]
    },
    shim: {
        bootstrap: ['jquery']
    }
});

requirejs(['plugins', 'modernizr-2.7.1', 'jquery', 'bootstrap'], function () {
    //<!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
    (function (b, o, i, l, e, r) {
        b.GoogleAnalyticsObject = l; b[l] || (b[l] =
        function () { (b[l].q = b[l].q || []).push(arguments) }); b[l].l = +new Date;
        e = o.createElement(i); r = o.getElementsByTagName(i)[0];
        e.src = '//www.google-analytics.com/analytics.js';
        r.parentNode.insertBefore(e, r)
    }(window, document, 'script', 'ga'));
    ga('create', 'UA-XXXXX-X'); ga('send', 'pageview');
});