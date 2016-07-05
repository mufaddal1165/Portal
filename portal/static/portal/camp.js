/**
 * Created by Mufaddal Tahir on 6/16/2016.
 */
$(function () {

    $("li").click(
        function () {
            $(this).addClass("active");
            $(this).siblings().removeClass("active");
            $(".navbar-brand").text($(this).text());
            var ind = $(this).index();
            $("#camp").val(ind + 1);
        }
    );
    $("#posttext").focus(
        function () {
            $(this).text(" ");
        }
    );
    $(".updatebutton").click(
      function () {

      }  
    );

});