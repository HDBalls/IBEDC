

var url_params ;
var urlparameters ;
var current_cmp ;

async function clearVcrContainer(){
    const garbages = ['#top','#oe_main_menu_navbar','#top_menu_container','#vcr'] //Mid two from Odoo Website Nav bar
    try{
        for (let garbage of garbages){
            var e = $(`${garbage}`);
            // $(e).remove();
        }   
    }
    catch(err){
        console.log(err)
    }
    
}

function ChangeUrl(pagedata,title,url) {
    if (typeof (history.pushState) != "undefined") {
        history.pushState(pagedata,title,url);
    } else {
        alert("Browser does not support HTML5.");
    }
}

function templateRenderer(data,mode){
    console.log("Found from db ",data, data.status)
   

    if ('content' in document.createElement('template')) {

        // Instantiate the table with the existing HTML tbody
        // and the row with the template
        console.log("Found from db ",data, data.status)
        if (data.status==false){
            var notfound_table = document.getElementById("norecord_found");
            var template = document.querySelector('#notfoundh1');
            // var clone = template.content.cloneNode(true);`                                                                                                                                                                                                                                                                                           -*
            var h1 = document.getElementById("notfoundh1");
            console.log("H1 ",h1)
            h1.style.display = 'flex';
            // h1.style.flexDirection = 'row'
            h1.innerHTML = data.message;
            // notfound_table.appendChild(clone);
            notfound_table.innerHTML = data.message ;
            notfound_table.style.display = 'block';
            return null
            
        }

        if (mode == 'billing'){
            var tbody = document.querySelector("tbody");
            var template = document.querySelector('#billingrow');
        
            // Clone the new row and insert it into the table
            var td = null
            var clone = null
            for (let i = 0; i<data.length;i++){
                clone = template.content.cloneNode(true);
                console.log("clone ",clone)
                td = clone.querySelectorAll("td");
                td[0].textContent = data[i][0];
                td[1].textContent = data[i][1];
                td[2].textContent = data[i][2];
                td[3].textContent = data[i][3];
                td[4].textContent = data[i][4];
                td[5].textContent = data[i][5];
                
            
                tbody.appendChild(clone);
            }
        }

        if (mode == 'payment'){
            console.log("Payment history ", data)
            var tbody = document.querySelector("tbody");
            var template = document.querySelector('#paymentrow');
        
            // Clone the new row and insert it into the table
            var td = null
            var clone = null
            for (let i = 0; i<data.length;i++){
                clone = template.content.cloneNode(true);
                console.log("clone ",clone, data[i])
                td = clone.querySelectorAll("td");
                td[0].textContent = data[i].initiation_date;
                td[1].textContent = data[i].timestamp;
                td[2].textContent = data[i].confirmation_date;
                td[3].textContent = data[i].units_consumed;
                td[4].textContent = data[i].transaction_id;
                td[5].textContent = data[i].transaction_refr;
                td[6].textContent = data[i].trans_status;
                td[7].textContent = data[i].gross_amount;
                td[8].textContent = data[i].net_amount;
            
                tbody.appendChild(clone);
            }
        }
        

    
    } else {
      // Find another way to add the rows to the table because
      // the HTML template element is not supported.
    }
}

function loadDashboardTemplate(template_id){
    clearVcrContainer().then(()=>{
        var user_url_params = OnInit(template_id)
        StateManagement.prototype.pushState('cms.curr.user',user_url_params)
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(dashboard_template.content.cloneNode(true));
        console.log("current user ", user_url_params)
        window.localStorage.setItem('current_url_id',template_id)
        
    })
    
}

function loadCustomerTemplate(template_id,loadType=false){
    if (loadType != "bodyload"){
        const queryString = window.location.search;
        // console.log("\n\nData from odoo server ",queryString);
        var fetchedState = StateManagement.prototype.pullState('cms.curr.user')
        console.log("\n\nUser state from Store ", fetchedState)
        clearVcrContainer().then(()=>{
            OnInit(template_id)
            let elem = document.getElementById('template_parent');
            console.log("b4 ",elem)
            let grock = document.getElementById('vcr');
            elem.append(customers_list_view.content.cloneNode(true));
            window.localStorage.setItem('cust_view_mode','list')
            // grock.append(elem);
            window.localStorage.setItem('current_url_id',template_id)
        })
    }

    if (loadType== 'bodyload'){
        const queryString = window.location.search;
        // console.log("\n\nData from odoo server ",queryString);
        var fetchedState = StateManagement.prototype.pullState('cms.curr.user')
        console.log("\n\nUser state from Store ", fetchedState)
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        console.log("after ",elem)
        let grock = document.getElementById('vcr');
        elem.append(customers_list_view.content.cloneNode(true));
        window.localStorage.setItem('cust_view_mode','list')

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
    

}

function parameters() {
    let url = window.location.href;
    console.log("url ",url)
    let paramString = new RegExp('(.*)[?](.*)').exec(url);
    if (null == paramString) {
      return {'base': url, 'params': null};
    }
  
    if (paramString[2].includes("&amp;")) {
      var paramList = paramString[2].split("&amp;");
    } else {
      var paramList = paramString[2].split("&");
    }
  
    let params = {};
    let appendable = ''
    for (let i = 0; i < paramList.length; i++) {
      var buffer = paramList[i]
      console.log(buffer)
      let values = paramList[i].split("=");
      console.log(buffer.charAt(buffer.length-1))
      appendable = "="
      params[values[0]] = values[1];
    //   if (buffer.charAt(buffer.length-1) == "="){
    //     appendable = "="
    //     params[values[0]] = values[1]+appendable;
    //   }
    //     else{
    //         params[values[0]] = values[1];
    //     }

      
    }
    return {"base": paramString[1], "params": params};
  }

function loadCustomerDetailsTemplate(template_id,url){
    
    url_params = parameters()
    urlparameters = url_params.params
    console.log(urlparameters)
    current_cmp = urlparameters.component
    clearVcrContainer().then(()=>{
        OnInit(template_id)
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(customer_details_template.content.cloneNode(true));
        window.localStorage.setItem('current_url_id',template_id)
        if (current_cmp == "personal_info"){
            loadPersonalInfoTemplate('personal_info_template')
        }
            
        if (current_cmp == "meter_info")
            loadMeteringInfoTemplate('meter_info_template')
        if (current_cmp == "assets_info")
            loadAssetsInfoTemplate('assets_info_template')
    })
    
    return null
    

}

function hasChildElement(elm) {
    var child, rv;
    if (elm.children) {
        // Supports `children`
        rv = elm.children.length !== 0;
    } else {
        // The hard way...
        rv = false;
        for (child = element.firstChild; !rv && child; child = child.nextSibling) {
            if (child.nodeType == 1) { // 1 == Element
                rv = true;
            }
        }
    }
    return rv;
}

async function clearInfoVcrContainer(id){
    var a = document.getElementById(`${id}`);
    if (hasChildElement(a)) {
        a.innerHTML=''
    }

}

function loadPersonalInfoTemplate(template_id){
    // clearInfoVcrContainer('info-vcr').then(()=>{
    //     OnInit(template_id)
    //     let elem = document.getElementById('info-vcr');
    //     elem.append(personal_info_template.content.cloneNode(true));
    //     window.localStorage.setItem('current_url_id',template_id)
    // })

    current_cmp = 'personal_info'
    OnComponentInit('personal_info').then(()=>{
        console.log("Loading Personal info template 1 ", template_id)
        clearInfoVcrContainer('info-vcr').then(()=>{
            OnInit(template_id)
            let elem = document.getElementById('info-vcr');
            elem.append(personal_info_template.content.cloneNode(true));
            window.localStorage.setItem('current_url_id',template_id)
            var newUrl = url_params.base+'?component=' + current_cmp+'&queryParam='+urlparameters.queryParam
            console.log("Change url to ",newUrl)
            ChangeUrl({state:'personal_info',data:urlparameters.queryParam},'Personal Information',newUrl);
        })
    })

} 

async function LoadSingleCustomerBilling(account_no){

    return new Promise(function(resolve, reject) {
        // var account_no = "11/12/64/0035-01"
        var url = `http://127.0.0.1:8069/cms/lazybilling_history/?account_no=${account_no}`
        fetch(url).then((response)=> {
            // console.log("Response from odoo backend ", JSON.stringify(response),response)
            return response.json();
            }).then((data)=> {
                
            if (data.status==true){
                console.log(data.data)
                resolve(data.data)
                return data.data
                //   alert(data.message) //reserve room for user
            }
            else{
                resolve(data)
                return data
                
            }
            
            }).catch(function(err) {
            console.log("Caught an error server ",err);
            });
        
    })
    
}

async function LoadSingleCustomerPayment(account_no){

    return new Promise(function(resolve, reject) {
        // var account_no = "11/12/64/0035-01"
        var url = `http://127.0.0.1:8069/cms/lazypayment_history/?account_no=${account_no}`
        fetch(url).then((response)=> {
            // console.log("Response from odoo backend ", JSON.stringify(response),response)
            return response.json();
            }).then((data)=> {
                
                if (data.status==true){
                    console.log(data.data)
                    resolve(data.data)
                    return data.data
                    //   alert(data.message) //reserve room for user
                }
                else{
                    resolve(data)
                    return data
                    
                }
            
            }).catch(function(err) {
            console.log("Caught an error server ",err);
            });
        
    })
    
}

function loadBillingInfoTemplate(template_id,account_no){
    clearInfoVcrContainer('info-vcr').then(()=>{
        OnInit(template_id)
        LoadSingleCustomerBilling(account_no).then((data)=>{
            console.log("Response ", data)
            let elem = document.getElementById('info-vcr');
            var p =  new Promise(function(resolve, reject) {
                resolve(elem.append(billing_history_info_template.content.cloneNode(true)))
            })
            p.then(()=>{
                setTimeout(() => templateRenderer(data,'billing'), 100);
                window.localStorage.setItem('current_url_id',template_id)
            })
            
        })
        
    })

}

function loadPaymentInfoTemplate(template_id,account_no){
    clearInfoVcrContainer('info-vcr').then(()=>{
        OnInit(template_id)
        LoadSingleCustomerPayment(account_no).then((data)=>{
            console.log("Response ", data)
            let elem = document.getElementById('info-vcr');
            var p =  new Promise(function(resolve, reject) {
                resolve(elem.append(payment_history_info_template.content.cloneNode(true)))
            })
            p.then(()=>{
                setTimeout(() => templateRenderer(data,'payment'), 100);
                window.localStorage.setItem('current_url_id',template_id)
            })
            
        })
    })

} 

async function OnComponentInit(current_cmp){
    if (current_cmp == 'meter_info'){
        console.log(`Rendering meter information template`)
        
    }
    if (current_cmp == 'personal_info'){
        console.log(`Rendering personal information template`)
        
    }
    if (current_cmp == 'assets_info'){
        console.log(`Rendering assets information template`)
        
    }
}

function loadMeteringInfoTemplate(template_id){
    current_cmp = 'meter_info'
    OnComponentInit('meter_info').then(()=>{
        console.log("Loading Meter info template 1 ", template_id)
        clearInfoVcrContainer('info-vcr').then(()=>{
            OnInit(template_id)
            let elem = document.getElementById('info-vcr');
            elem.append(meter_info_template.content.cloneNode(true));
            window.localStorage.setItem('current_url_id',template_id)
            var newUrl = url_params.base+'?component=' + current_cmp+'&queryParam='+urlparameters.queryParam
            console.log("Change url to ",newUrl)
            ChangeUrl({state:'meter_info',data:urlparameters.queryParam},'Meter Information',newUrl);
        })
    })
    
    
} 

function loadAssetsInfoTemplate(template_id){
    current_cmp = 'assets_info'
    OnComponentInit('assets_info').then(()=>{
        console.log("Loading assets info template 1 ", template_id)
        clearInfoVcrContainer('info-vcr').then(()=>{
            OnInit(template_id)
            let elem = document.getElementById('info-vcr');
            elem.append(assets_info_template.content.cloneNode(true));
            window.localStorage.setItem('current_url_id',template_id)
            var newUrl = url_params.base+'?component=' + current_cmp+'&queryParam='+urlparameters.queryParam
            console.log("Change url to ",newUrl)
            ChangeUrl({state:'assets_info',data:urlparameters.queryParam},'Assets Information',newUrl);
        })
    })
    
    
} 



// for (var a=[],i=0;i<40;++i) a[i]=i; for older browsers

// function shuffle(array) {
//   var tmp, current, top = array.length;
//   if(top) while(--top) {
//     current = Math.floor(Math.random() * (top + 1));
//     tmp = array[current];
//     array[current] = array[top];
//     array[top] = tmp;
//   }
//   return array;
// }

// a = shuffle(a);
function randomArray(length, max) {
    return Array.apply(null, Array(length)).map(function() {
        return Math.round(Math.random() * max);
    });
}

function encryptString(value){
    var secret = new fernet.Secret("5CWvxbkxPI2e0W2KRc1l4ZXMXRn7WJzdGP9NZhbbVgA=");
    var arr = randomArray(15,1000)
    console.log("\n\nencryption array ",arr)
    return new fernet.Token({
        secret: secret,
        time: Date.parse(1),
        iv: arr
      }).encode(value)
}

function decryptString(value){
    value = value.replace(/@/g,"=")
    console.log("REplaceing ", value)
    var secret = new fernet.Secret("5CWvxbkxPI2e0W2KRc1l4ZXMXRn7WJzdGP9NZhbbVgA=");
    return new fernet.Token({
        secret:secret,
        token:`${value}`,
        ttl:0
    }).decode();
}

function navigateToCustomerDetailsTemplate(domObj,component){
    var vals = domObj.getAttribute("value").split('[')[1].split(']')[0].split("'")
    console.log(vals[1].split("'")[0],vals[3].split("'")[0])
    var queryParam = vals[1].split("'")[0]
    var component = vals[3].split("'")[0]
    var token = decryptString(queryParam)
    console.log("Decoded token ",token)
    document.location.replace(`/cms/customer_details?component=${component}&queryParam=${queryParam}`)
}

function listmode(){
    window.localStorage.setItem('cust_view_mode','list')

    clearInfoVcrContainer('template_parent').then(()=>{
        let elem = document.getElementById('template_parent');
        let grock = document.getElementById('vcr');
        elem.append(customers_list_view.content.cloneNode(true));
        var isVal = document.getElementById("search_customer_input").value
        console.log("When empty ",isVal)
        if (isVal){
            console.log('search Has val')
            searchCustomer()
        }
        else{
            console.log("search empty")
        }
    })
}

function gridmode(){
    window.localStorage.setItem('cust_view_mode','grid')
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
        var isVal = document.getElementById("search_customer_input").value
        console.log("When empty ",isVal)
        if (isVal){
            console.log('search Has val')
            searchCustomer()
        }
        else{
            console.log("search empty")
        }
        // searchCustomer()
    // })
    

}

function OnInit(template_id){
    try{
        var a = $('#oe_main_menu_navbar');
        $(a).remove();

        var b = $('#top_menu_container');
        $(b).remove();
        
        var h = $('#top');
        $(h).remove();

        var route = window.localStorage.getItem('current_url_id')
        if(route==null){
            window.localStorage.setItem('current_url_id',template_id)
        }
        console.log("Current route ",route)
        return parameters()
    }
    catch(err){
        window.localStorage.setItem('current_url_id',template_id)
    }
}

function searchCustomer() {
    var view_mode = window.localStorage.getItem('cust_view_mode')
    if (view_mode == "list"){
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("search_customer_input");
        filter = input.value.toUpperCase();
        table = document.getElementById("customers_table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
            } else {
            tr[i].style.display = "none";
            }
            }       
        }
    }

    if (view_mode == "grid"){

        var input, filter, grid, div, td, i, txtValue,name;
        input = document.getElementById("search_customer_input");
        filter = input.value.toUpperCase();
        grid = document.getElementById("customers_grid");
        for (i = 0; i < grid.childElementCount; i++) {
        div = grid.children[i]
        divt = div.getElementsByTagName("div")[7];
        // console.log("chosen div ", divt)
        // console.log('Div I',div)
        name = div.getElementsByTagName("span")[1];
        // console.log('Name ',name)
        if (name) {
            txtValue = name.textContent || name.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
            div.style.display = "";
            } else {
            div.style.display = "none";
            }
        }       

    }   
    }
    
  }


function searchPaymentHistory() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search_payment_input");
    filter = input.value.toUpperCase();
    table = document.getElementById("payment_table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }


  function searchBillHistory() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search_bill_input");
    filter = input.value.toUpperCase();
    table = document.getElementById("bill_table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }

  function exportTableToExcels(tableID, filename = ''){
    var downloadLink;
    var dataType = 'application/vnd.ms-excel';
    var tableSelect = document.getElementById(tableID);
    var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');
    
    // Specify file name
    filename = filename?filename+'.xls':'excel_data.xls';
    
    // Create download link element
    downloadLink = document.createElement("a");
    
    document.body.appendChild(downloadLink);
    
    if(navigator.msSaveOrOpenBlob){
        var blob = new Blob(['\ufeff', tableHTML], {
            type: dataType
        });
        navigator.msSaveOrOpenBlob( blob, filename);
    }else{
        // Create a link to the file
        downloadLink.href = 'data:' + dataType + ', ' + tableHTML;
    
        // Setting the file name
        downloadLink.download = filename;
        
        //triggering the function
        downloadLink.click();
    }
}


function exportTableToExcel(tableID, filename = '', fn, dl,type='xlsx') {
    var elt = document.getElementById(tableID);
    var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
    return dl ?
      XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
      XLSX.writeFile(wb, fn || (filename));
 }

function redirect(view){
    if (view == "dashboard"){
        var fetchedState = StateManagement.prototype.pullState('cms.curr.user').params
        console.log("decrypted id ",fetchedState.id,decryptString(fetchedState.id))
        document.location.replace(`/cms/dashboard/?view=${'dashboard'}&id=${fetchedState.id}&user=${fetchedState.user}`)
    }
    if (view == "customers"){
        var fetchedState = StateManagement.prototype.pullState('cms.curr.user').params
        document.location.replace(`/cms/customers/?view=${'customers'}&id=${fetchedState.id}&user=${fetchedState.user}`)
    }
    if (view == "billing_history"){
        var fetchedState = StateManagement.prototype.pullState('cms.curr.user').params
        console.log("decrypted id ",fetchedState.id,decryptString(fetchedState.id))
        document.location.replace(`/cms/billing_history/?view=${'billing_history'}&id=${fetchedState.id}&user=${fetchedState.user}`)
    }
    if (view == "payment_history"){
        var fetchedState = StateManagement.prototype.pullState('cms.curr.user').params
        document.location.replace(`/cms/payment_history/?view=${'payment_history'}&id=${fetchedState.id}&user=${fetchedState.user}`)
    }
}


// [2022-05-14T01:12:15.350Z]  "GET /chart_meter_statistics.js" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"       
// [2022-05-14T01:12:16.850Z]  "GET /ibedc_logo.png" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
// [2022-05-14T01:31:49.300Z]  "GET /graph.png" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
// [2022-05-14T01:31:49.302Z]  "GET /graph_red.png" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"