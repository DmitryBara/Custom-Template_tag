$(document).ready( () => {

      // Disable ajax block when ajax request wasn't done
      $('#ajaxContent').find("*").prop('disabled',true);


      // Clear url saved in history cache
       var baseUrl = 'http://localhost:8000/';
        $.ajaxSetup({
          crossDomain: false,
          beforeSend: function(xhr, options) {
              options.url = baseUrl + options.url;
          }
        })


        console.log('MenuId const array: ', menuId)
        


      $('li').on('click', function (e) {

          e.stopPropagation();
          e.preventDefault();

          var $this = $(this)
          var url_ajax = $this.children('a').first().attr('href')

          $.ajax({
              url: url_ajax,
              method: 'GET',

              // Load Ajax component and change browser url adress
              success: function(d) {
                  $('.ajaxContent').html(d)
                  history.pushState(null, null, 'http://localhost:8000/' + url_ajax);
              },
              error: function(d) {
                console.log('Error: ', d);
              }
          });
      });
})