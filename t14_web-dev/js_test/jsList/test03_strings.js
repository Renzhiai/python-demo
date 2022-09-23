/**
 * Created by Administrator on 2017/3/15.
 */
s='跑马的汉子，你威武雄壮 '
function loop(){
    document.getElementById('light').innerHTML=s
    //document.write(s)
    //document.write('<br/>')
    var len=s.length
    s=s.substring(1,len)+s.substring(0,1)
    //document.write(s)
}
//loop()
setInterval(loop,800);
