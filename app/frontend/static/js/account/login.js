require.config({
    paths: {
        jquery: ['https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min', 'jquery-1.10.2.min']
    }
});

require(['jquery', 'hash', 'account/seed'], function (jq, hash, seed) {
    $('#loginForm_submit').click(function () {
        var rseed = seed();
        var useed = seed($('#username').val());
        if (useed != '') {
            var password = $('#password');
            var pw = hash(password.val() + useed).toString();
            password.val(hash(pw + rseed).toString());
            $('#loginForm').submit();
        } else {
            $('#error').text('User does not exist.');
        }
    });
});
