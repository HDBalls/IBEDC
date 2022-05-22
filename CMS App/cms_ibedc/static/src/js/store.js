
var Store = window.localStorage

 class StateManagement{ //Simple store 

    
    pushState(key,value){
        Store.setItem(key,JSON.stringify(value));
    }

    pullState(key){
        var  _ = Store.getItem(key)
        return JSON.parse(_)
    }


}






