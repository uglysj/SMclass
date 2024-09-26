$(function(){ // jquery
  $("#searchBtn").click(function(){ // searchBtn
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=UWVntvJMCXNFBgOb8rJ6bmTL0Vhdr66tlDa%2FUhQbhJiARcEI3XVr%2FjuTqnZ%2B%2Fj4kNwB5G1yDiny2zEiJGUttBg%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({ //ajax
      url: surl,
      type: "get",
      data: "",
      dataType: "json",
      success: function(data){
        alert("성공");
        // console.log(data);
        var g_item = data.response.body.items.item;
        var n_data = "";

        for(var i = 0; i < g_item.length; i++){
          n_data += `<tr id='${g_item[i].galContentId}'>`;
          n_data += `<td>${g_item[i].galContentId}</td>`;
          n_data += `<td>${g_item[i].galTitle}</td>`
          n_data += `<td>${g_item[i].galPhotographer}</td>`
          n_data += `<td>${g_item[i].galModifiedtime}</td>`
          n_data += `<td><img src='${g_item[i].galWebImageUrl}'</td>`
          n_data += `</tr>`;
        }
        // $("tbody").append(n_data);
        $("tbody").html(n_data);
      },
      error: function(){
        alert("실패");
      }
    }); // ajax
  }); // searchBtn
}); // jquery