import { setUsername, setNavBorder } from './main.js'

export class DashboardTemplate{

    constructor(){}

    loadDashboardTemplate(template_id){
        clearVcrContainer().then(()=>{
            var user_url_params = OnInit(template_id)
            StateManagement.prototype.pushState('cms.curr.user',user_url_params)
            let elem = document.getElementById('template_parent');
            let grock = document.getElementById('vcr');
            elem.append(dashboard_template.content.cloneNode(true));
            window.localStorage.setItem('current_url_id',template_id) 
            setUsername() 
            setNavBorder(0) 
            
        })
        
    }
        
}
