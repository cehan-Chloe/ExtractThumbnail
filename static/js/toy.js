function getThumbnail() {
  video_url = $("#url_input").val().replace(/ +?/g, '');
  data = {
    url: video_url,
  };

  $.ajax({
    url: "http://localhost:8080/get_thumbnail",
    type: 'GET',
    data: data,
    dataType: "json",
    success: function success(data) {
      image_path = "static/img/" + data.image_name;
      $("#img_div").html("<img src=\"" + image_path + "\" style=\"width:50\%\;height\:auto\;\">");
    },
    error: function error(xhr,status,error) {
      $("#img_div").html("<p> There is an error happened: " + error +" </p>");
    }
  });

}