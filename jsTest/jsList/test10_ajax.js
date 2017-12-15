/**
 * Created by Administrator on 2017/3/15.
 */
var ajaxreq=false
var ajaxCallback
function ajaxRequest(filename){
    try{
        //Firefox/IE7/Others
        ajaxreq=new XMLHttpRequest()
    }catch(error){
        try{
            //IE5/IE6
            ajaxreq=new ActiveXObject('Microsoft.XMLHTTP')
        }catch(error){
            return false
        }
    }
    ajaxreq.open('GET',filename);
    ajaxreq.onreadystatechange=ajaxResponse
    ajaxreq.send(null)
}
function ajaxResponse(){
    if(ajaxreq.readyState!=4){
        return
    }
    if(ajaxreq.status==200){
        // done
        if(ajaxCallback){
            ajaxCallback()
        }else{
            alert('Request failed:'+ajaxreq.statusText)
            return true
        }
    }
}