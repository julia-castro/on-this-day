$( document ).ready(function() {
  $( ".tab" ).on( "click", function() {
    var section = $(this).data( "section" );
    var articles = $('.article-information');

    for (i = 0; i < articles.length; i++) {
      var data = $(articles[i]).data("section")
      if (data === section) {
        $(articles[i]).show()
      } else {
        $(articles[i]).hide()
      }
    }
  });
});
