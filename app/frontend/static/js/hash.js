//CryptoJS provides JavaScript implmentations of popular encryption algorithms
// This javascript module returns the currently selected encryption method.
// Changing the encryption method returned by the module will change the encryption method used
// by every JavaScriptmodule that references this module.
// The paths provide CDN resources for each of the methods.

require.config({
    paths: {
        md5: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/md5',
        sha1: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha1',
        sha256: ['http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha256', 'sha256'],
        sha512: 'http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/sha512'
    }
});

define(['sha256'], function () {
    return CryptoJS.SHA256;
});