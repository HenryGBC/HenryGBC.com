$(function(){

	$( "pre" ).addClass( "prettyprint" );
	 

	/***********Contactame**************/
	$('#send').on('click', function(event){
			event.preventDefault();
	 		
	 		var name = $('#nameInput').val();
	 		var email = $('#emailInput').val();
	 		var message = $('#messageText').val();

	 	
	 		$.ajax({

                data : {'name': name,'email': email, 'message': message},
                url : 'contact/',
                type : 'post',

             });
	 		
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