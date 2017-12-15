/**
 * Created by Administrator on 2017/3/16.
 */
var qn=0
var ajaxreq=false
var ajaxCallback
function ajaxRequest(filename) {
    try {
        //Firefox/IE7/Others
        ajaxreq = new XMLHttpRequest()
    } catch (error) {
        try {
            //IE5/IE6
            ajaxreq = new ActiveXObject('Microsoft.XMLHTTP')
        } catch (error) {
            return false
        }
    }
    ajaxreq.open('GET', filename);
    ajaxreq.onreadystatechange=ajaxResponse
    ajaxreq.send()
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

function getQuestions(){
    obj=document.getElementById('question')
    obj.firstChild.nodeValue='(please wait)'
    ajaxCallback=nextQuestion
    ajaxRequest('questions.xml')
}
function nextQuestion(){
    questions=ajaxreq.responseXML.getElementsByTagName('q')
    obj=document.getElementById('question')
    if(qn<questions.length){
        q=questions[qn].firstChild.nodeValue
        obj.firstChild.nodeValue=q
    }else{
        obj.firstChild.nodeValue='(no more questions)'
    }
}
function checkAnswer(){
    answers=ajaxreq.responseXML.getElementsByTagName('a')
    a=answers[qn].firstChild.nodeValue
    answerfield=document.getElementById('answer')
    if(a==answerfield.value){
        alert('Correct!')
    }else{
        alert('Incorrect.The answer is: '+a)
    }
    qn=qn+1
    answerfield.value=''
    nextQuestion()
}

obj=document.getElementById('start')
obj.onclick=getQuestions
ans=document.getElementById('submit')
ans.onclick=checkAnswer