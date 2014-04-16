$(function(){

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



});