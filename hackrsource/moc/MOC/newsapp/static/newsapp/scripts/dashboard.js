function search(){
	tags = document.getElementById("search-text").value
	if(tags == ""){
		alert("The tags field is empty");
	}
	else{
		$.ajax({
			type:"GET",
			url:"search",
			data:{
				value:tags
			},
			success : function(data) {
				$('#post-list').html(data);
			}
		});
	}
}

$(function() {

    $('#login-form-link').click(function(e) {
		$("#login-form").delay(100).fadeIn(100);
 		$("#register-form").fadeOut(100);
		$('#register-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#register-form-link').click(function(e) {
		$("#register-form").delay(100).fadeIn(100);
 		$("#login-form").fadeOut(100);
		$('#login-form-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});
