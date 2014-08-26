$(function(){

	$( "pre" ).addClass( "prettyprint" );
	 $('#alert').hide()
	 $('#enviar').on('click', function(event){
			event.preventDefault();
	 		
	 		var email = $('#email_input').val();

	 		$.ajax({

                data : {'email': email},
                url : 'email/',
                type : 'post',

             });
	 		$('#email_input').val(' ');
	 		$('#alert').fadeIn()
	 });

	 $('#close').on('click', function(event){
			$('#alert').fadeOut()
	 });


/******************Isotope****************/

 var $container = $('.skillContainer').isotope({
 	containerStyle: { position: 'relative'},
    itemSelector: '.skill-item',
    layoutMode: 'fitRows',
  });

  $('#filters').on( 'click', 'button', function() {
    var filterValue = $( this ).attr('data-filter');
    // use filterFn if matches value
    //filterValue = filterFns[ filterValue ] || filterValue;
    $container.isotope({ filter: filterValue });
  });

/*****************Initialize Masonry************/

	var $containerPost = $('.postContainer');
	// initialize
	$containerPost.masonry({
	  columnWidth: 5,
	  itemSelector: '.post'
	});

});