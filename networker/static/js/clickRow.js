// provides the functionality to make a table linkable
$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
}); 
	
