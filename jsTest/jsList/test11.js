/**
 * Created by Administrator on 2017/3/16.
 */
setTimeout('a()',2000)
function a(){
    document.getElementsByName('userName').click()
    document.getElementsByName('userName').value='test'
    alert(document.getElementsByName('userName').value)
}
