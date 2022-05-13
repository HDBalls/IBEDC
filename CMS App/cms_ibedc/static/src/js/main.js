async function clearVcrContainer(){
    
    try{
        var a = $('#vcr');
        $(a).remove();
    }
    catch(err){
        console.log(err)
    }
    
}

function loadDashboardTemplate(template_id){
    clearVcrContainer().then(()=>{
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(dashboard_template.content.cloneNode(true));
        grock.append(elem);
        window.localStorage.setItem('current_url_id',template_id)
        
    })
    

}

function loadCustomerTemplate(template_id,loadType=false){
    if (loadType != "bodyload"){
        clearVcrContainer().then(()=>{
            OnInit(template_id)
            let elem = document.getElementById('template_parent');
            console.log("b4 ",elem)
            let grock = document.getElementById('vcr');
            elem.append(customers_list_view.content.cloneNode(true));
            grock.append(elem);
            window.localStorage.setItem('current_url_id',template_id)
        })
    }

    if (loadType== 'bodyload'){
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        console.log("after ",elem)
        let grock = document.getElementById('vcr');
        elem.append(customers_list_view.content.cloneNode(true));
        grock.append(elem);
        window.localStorage.setItem('current_url_id',template_id)
    }
    
    

}


function loadBillingHistoryTemplate(template_id){
    clearVcrContainer().then(()=>{
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(billinghistory_template.content.cloneNode(true));
        grock.append(elem);
        window.localStorage.setItem('current_url_id',template_id)
    })
    

}

function loadPaymentsHistoryTemplate(template_id){
    clearVcrContainer().then(()=>{
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(paymentshistory_template.content.cloneNode(true));
        grock.append(elem);
        window.localStorage.setItem('current_url_id',template_id)
    })
    

}function loadCustomerDetailsTemplate(template_id){
    clearVcrContainer().then(()=>{
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(customer_details_template.content.cloneNode(true));
        // grock.append(elem);
        window.localStorage.setItem('current_url_id',template_id)
        
    })

}

function navigateToCustomerDetailsTemplate(event){
    console.log(event.target.value)
    document.location.replace(`/cms/customer_details?queryParam=${event.target.value}`)
}

async function checkForDates(value){
    value = '09/09/2022'
    var url = `http://127.0.0.1:5000/getdate?date=${value}`
    fetch(url).then(function(response) {
        return response.json();
      }).then(function(data) {
        console.log(data);
        if (data.status==true){
            alert("Time frame is available")
        }
        else{
            alert("Time frame is not available")
        }
        
      }).catch(function() {
        console.log("Caught an error from flask server request");
      });
}

function gridmode(){
    // clearVcrContainer().then(()=>{
        try{
            var a = $('#list-card');
            $(a).remove();
        }
        catch(err){
            console.log(err)
        }
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(tmpl.content.cloneNode(true));
        grock.append(elem);
    // })
    

}

function OnInit(template_id){
    try{
        var route = window.localStorage.getItem('current_url_id')
        if(route==null){
            window.localStorage.setItem('current_url_id',template_id)
        }
        console.log("Current route ",route)
    }
    catch(err){
        window.localStorage.setItem('current_url_id',template_id)
    }
}

