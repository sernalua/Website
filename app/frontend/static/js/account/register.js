require.config({
    urlArgs: 'nocache=' + (new Date()).getTime(),
    paths: {
        md5: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/md5',
        sha1: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha1',
        sha256: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha256',
        sha512: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha512',
        jquery: ['https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min', 'jquery-1.10.2.min']
    }
});

require(['jquery', 'hash', 'account/seed'], function (jq, hash, seed) {
    $('#registerForm_submit').click(function () {
        $('#error').text('');
        var rseed = seed();
        var password = $('#password');
        var password_confirmation = $('#password_confirmation');
        if (password.val() == password_confirmation.val()) {
            var pw = hash(password.val() + rseed).toString();
            password.val(pw);
            password_confirmation.val(pw);
            $('#registerForm').submit();
        } else {
            $('#error').text('Passwords do not match.');
        }
    });
});
