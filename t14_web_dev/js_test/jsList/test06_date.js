/**
 * Created by Administrator on 2017/3/15.
 */
now=new Date();
hours=now.getHours();
mins=now.getMinutes();
secs=now.getSeconds();
year=now.getFullYear();
month=now.getMonth()+1;   //得到月份数-1
day=now.getDate();
weekday=now.getDay();   //得到星期几
if(hours<10){
    hours=hours+'';
    hours='0'+hours
}
if(mins<10){
    mins=mins+'';
    mins='0'+mins
}
if(secs<10){
    secs=secs+'';
    secs='0'+secs
}
document.write('<h2>');
document.write(hours+':'+mins+':'+secs);
document.write('</h2>');
document.write('<p>');
document.write(year+'-'+month+'-'+day);
document.write('</p>');