/*!
* mysite v0.0.1 (https://github.com/willem-vanheemstrasystems/django-frontend.git)
*
* Copyright 2013-2015 vanheemstrasystems
* Licensed under MIT (https://github.com/willem-vanheemstrasystems/django-frontend/blob/master/LICENSE)
*/

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module unless amdModuleId is set
    define(["jquery"], function (a0) {
        return (factory(a0));
    });
    } else if (typeof exports === 'object') {
    // Node. Does not work with strict CommonJS, but
    // only CommonJS-like environments that support module.exports,
    // like Node.
    module.exports = factory(require("jquery"));
    } else {
    factory(jQuery);
    }
}(this, function (jQuery) {

(function ($) {
    'use strict';

    console.log("mysite.js called");
    
    
    
})(jQuery);

}));