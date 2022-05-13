odoo.define('js_hide_settings', function (require) {
    "use strict";
    var rpc = require('web.rpc');
    console.log("call from javascript ")
    rpc.query({
        model:'res.users',
        method:'serve',
        args:[1]
    }).then((result)=>{
        console.log("Result from javascript ", result)
        if (result){
            let selection = document.getElementById('o_field_input_735')
            selection.style.display === "none";
        }

    })
  
    // some code
    return true;
  });