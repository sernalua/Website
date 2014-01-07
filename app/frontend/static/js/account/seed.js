require.config({
    paths: {
        jquery: ['https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min', 'jquery-1.10.2.min']
    }
})

define(['jquery'], function (jq) {
    return function (user) {
        var seed = '';
        $.ajax({
            url: '/api/seed/' + (user != null ? user + '/': ''),
            async: false,
            cache: false
        }).done(function (value) {
            seed = value;
        });
        return seed;
    }
});