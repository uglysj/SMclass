let sum = 0; // 합계
let avg = 0; // 평균
let cnt = 0; // 인원 카운트
let b_check = 0; // 버튼 확인용
let tr_id;

$(function(){ // 제이쿼리
  $("#dataBtn").click(function(){ // 데이터 가져오기 버튼
    alert("데이터를 가져옵니다.");
    $.ajax({ // ajax
      url: "js/stuData.json",
      type: "get",
      data: "",
      dataType: "json",
      success: function(data){
        let student;

        for(var i = 0; i < data.length; i++){
          sum = data[i].kor + data[i].eng + data[i].math;
          avg = (sum / 3).toFixed(2);

          // 표 형식에 맞게 데이터 저장
          student += `<tr id='${data[i].no}'>`;
          student += `<td>${data[i].no}</td>`
          student += `<td>${data[i].name}</td>`
          student += `<td>${data[i].kor}</td>`
          student += `<td>${data[i].eng}</td>`
          student += `<td>${data[i].math}</td>`
          student += `<td>${sum}</td>`
          student += `<td>${avg}</td>`
          student += `<td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>`
          student += `</tr>`

          cnt++;
        }
        $("#tbody").html(student); // tobdy에 student 값 넣기
      },
      error: function(){
        alert("실패");
      }
    }); // ajax
  }); // 데이터 가져오기 버튼

  $(document).on("click", "#create", function(){ // 추가 버튼
    // input 태그 안에 값 가져오기
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());

    sum = kor + eng + math;
    avg = (sum / 3).toFixed(2);

    // input 태그 안에 데이터가 있는지 검사
    if(name == "" || $("#kor").val().length < 1 || $("#eng").val().length < 1 || $("#math").val().length < 1){
      alert("데이터를 채워 주셔야 추가가 가능합니다.");
      return false;
    } else if(isNaN(kor) == true || isNaN(eng) == true || isNaN(math) == true){ // 성적에 문자가 있는지 검사
      alert("성적은 숫자로 입력해주세요");
      return false;
    } else if(isNaN(name) == false){ // 이름에 숫자가 있는지 검사
      alert("이름은 문자로 입력해주세요");
      return false;
    }

    alert(`${name} 학생을 추가 합니다.`);
    cnt++;
    
    // 표 맨 밑에 데이터 추가
    let student;
    student += `<tr id=${cnt}>`;
    student += `<td>${cnt}</td>`;
    student += `<td>${name}</td>`;
    student += `<td>${kor}</td>`;
    student += `<td>${eng}</td>`;
    student += `<td>${math}</td>`;
    student += `<td>${sum}</td>`;
    student += `<td>${avg}</td>`;
    student += `<td><button class='updateBtn'>수정</button><button class='delBtn'>삭제</button></td>`;
    student += `</tr>`;
    $("#tbody").append(student);

    $("#name, #kor, #eng, #math").val(""); // input 태그 안에 공백 처리
  }); //추가 버튼

  $(document).on("click", ".updateBtn", function(){ // 수정버튼
    tr_id = $(this).closest("tr").attr("id");

    if(b_check === 1){ // 수정버튼이 클릭되어 있는지 확인
      alert("수정완료 또는 수정취소를 누르셔야 합니다.");
      return false;
    } else {
      $(this).css({"color": "red", "font-weight": "700"});
      $("#create, #update, #updateCancel").toggle(); // 버튼 추가 삭제
      alert(`${tr_id}번 학생을 수정합니다.`);
      // 표에 있는 값 input 태그로 출력
      $("#name").val($("#"+tr_id).children("td:eq(1)").text());
      $("#kor").val($("#"+tr_id).children("td:eq(2)").text());
      $("#eng").val($("#"+tr_id).children("td:eq(3)").text());
      $("#math").val($("#"+tr_id).children("td:eq(4)").text());
    }
    $(document).scrollTop(0); // 최상단으로 이동
    b_check = 1; // 수정버튼 눌린 상태
  }); // 수정 버튼

  $(document).on("click", "#update", function(){ // 수정완료 버튼
    // input 태그 안에 값 가져오기
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());

    sum = kor + eng + math;
    avg = (sum / 3).toFixed(2);

    // input 태그 안에 데이터가 있는지 검사
    if(name == "" || kor == "" || eng == "" || math == ""){
      alert("데이터를 채워 주셔야 추가가 가능합니다.");
      return false;
    } else if(isNaN(kor) == true || isNaN(eng) == true || isNaN(math) == true){
      alert("성적은 숫자로 입력해주세요");
      return false;
    } else if(isNaN(name) == false){
      alert("이름은 문자로 입력해주세요");
      return false;
    } else alert("수정 완료 되었습니다.");

    // 수정한 데이터 표 안으로 이동
    $("#"+tr_id).children("td:eq(1)").text($("#name").val());
    $("#"+tr_id).children("td:eq(2)").text($("#kor").val());
    $("#"+tr_id).children("td:eq(3)").text($("#eng").val());
    $("#"+tr_id).children("td:eq(4)").text($("#math").val());
    $("#"+tr_id).children("td:eq(5)").text(sum);
    $("#"+tr_id).children("td:eq(6)").text(avg);

    $("#name, #kor, #eng, #math").val(""); // input 태그 안에 공백 처리
    $("#create, #update, #updateCancel").toggle(); // 버튼 추가 삭제
    b_check = 0; // 수정버튼 초기화
    $(".updateBtn").css({"color": "black", "font-weight": "400"});
  }); // 수정 완료 버튼

  $(document).on("click", "#updateCancel", function(){ // 수정취소 버튼
    alert("수정을 취소합니다.");
    $("#name, #kor, #eng, #math").val(""); // input 태그 안에 공백 처리
    $("#create, #update, #updateCancel").toggle(); // 버튼 추가 삭제
    b_check = 0; // 수정버튼 초기화
    $(".updateBtn").css({"color": "black", "font-weight": "400"});
  }); // 수정 취소 버튼

  $(document).on("click", ".delBtn", function(){ // 삭제버튼
    tr_id = $(this).closest("tr").attr("id");

    if(confirm(`${tr_id}번 학생을 삭제하시겠습니까?`)) $("#"+tr_id).remove();
  }); // 삭제 버튼
}); // 제이쿼리