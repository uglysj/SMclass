let num = 0;
let num2 = 0;
$(function(){ // jquery
  $("#right").click(function(){ // right 버튼
    // alert("우측버튼 클릭");
    if(num >= 900){
      alert("오른쪽 끝");
      return false;
    }
    $("#box").stop();
    num += 100;
    num2 += 360;
    $("#box").animate({
      left: num, rotate: num2 + "deg"
    }, 1000);
  }); // right 버튼
  
  $("#left").click(function(){ // left 버튼
    // alert("좌측버튼 클릭");
    if(num <= 0){
      alert("왼쪽 끝");
      return false;
    }
    $("#box").stop();
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left: num, rotate: num2 + "deg"
    }, 1000);
  }); // left 버튼
}); // jquery