var checkboxes = [];
var preferences = {}
var key ,parent;

function loadTransientFields(view) {
    

    // event listener on change
    $('input[type=checkbox]').on('change', function(){
        parent =  $(this).closest('table').attr('id');
        checkboxes.push($(this).val());
    });
    
    document.getElementById("myDropdown").classList.toggle("show");
  }
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn') && !event.target.matches('.item') && !event.target.matches('.material-icons')) {
      
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          if (checkboxes.length > 0){
           
            var status = confirm("Do you want to save changes ?")
            if (status == true){
              $("input[type=checkbox]").each(function () {
                console.log($(this))
                key = $(this)[0].id
                preferences[[key]] = $(this)[0].checked
              });
              console.log("All checkboxes ",preferences, parent);
              savePreferences(parent,preferences)
              openDropdown.classList.remove('show');
              checkboxes = []
            }
            else{
              openDropdown.classList.remove('show');
            }
          }
          else{
            checkboxes = []
            openDropdown.classList.remove('show');
          }
          
          
        }
      }
    }
  }


function savePreferences(field,preferences){
  preferences = JSON.stringify(preferences)
  return new Promise(function(resolve, reject) {
    var url = `http://127.0.0.1:8069/cms/preferences/?field=${field}&preferences=${preferences}`
    fetch(url).then((response)=> {

        return response.json();
        }).then((res)=> {resolve(res.status)}).catch(function(err) {
        console.log("Caught an error server ",err);
        });

})
}