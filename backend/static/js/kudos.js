
/***************************************
*  THE MAGIC INGREDIENT
***************************************/


$(document).ready(function() {  

  function addKudos(endpoint){
    $('iframe').src("");
    $('iframe').src(endpoint);
  }


  $(".kudos").click(function(e){
    endpoint = $(this).attr("href");
    addKudos(endpoint);
    e.preventDefault();
    $(this).hide();
    return false;
  });
});
