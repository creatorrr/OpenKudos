
/***************************************
*  THE MAGIC INGREDIENT
***************************************/

/* WHAT THIS DOES:
*  - Updates stats for all kudos buttons.
*  - Looks for mouseenter on all kudos buttons.
*  - Catches URL from nested a tag
*  - Makes get request to the url
*  - And marks button as done.
*/



$(document).ready(function() {  

  function addKudos(endpoint, button){
    $(button).find('iframe').src("");
    $(button).find('iframe').src(endpoint);
    console.log(button);
  }

   $("figure.kudos_button").each(function(){
             endpoint = $(this).find('a').attr("href").replace("incr","stats").replace("decr","stats");
             $(this).find('iframe').src("");
             $(this).find('iframe').src(endpoint);
                 console.log(this);
                        });


  $("figure.kudos_button").click(function(e){
    e.preventDefault();
    return false;
  });

  // The hover selector is the best thing ever.
  var t;
  var x;
  $("figure.kudos_button").mouseenter(
    function () {
      clearTimeout(t); //Cancel and restart.
      
      $(this).find('iframe').hide();

      var endState = $.proxy(function(){
        $(this).find('div.filled').hide();

        if(!$(this).hasClass('done')){
          endpoint = $(this).find('a').attr("href");
          addKudos(endpoint, this);
          $(this).removeClass('waiting').addClass('done');
        }
        $(this).removeClass('waiting').addClass('done');
      },$(this));

    t=setTimeout(endState, 1000); //run the animation for exactly one second, then fire the action
  }).mouseleave(function(){
    clearTimeout(t); //cancel when the mouse falls away
    if(!$(this).hasClass('done')){
      $(this).removeClass('done').addClass('waiting').show();
      $(this).find('iframe').show(); // and return the description
    }
  });
});

