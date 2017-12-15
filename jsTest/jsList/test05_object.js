/**
 * Created by Administrator on 2017/3/15.
 */

function PrintStudent(){
    line1="<b>Name:</b>"+this.name+"<br/>\n";
    line2="<b>Sex:</b>"+this.sex+"<br/>\n";
    line3="<b>Score:</b>"+this.score+"<br/>\n";
    document.write(line1,line2,line3);
}
function Student(name,sex,score){
    this.name=name;
    this.sex=sex;
    this.score=score;
    this.PrintStudent=PrintStudent;
}

var tom=new Student("Tom","male",85);
tom.PrintStudent();