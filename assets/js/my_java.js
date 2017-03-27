function add_request_number(){
	$.ajax({
		type:"GET",
		url:"/request_number",
		data:{},
		
		success:function(json){
            $('title').text('Request ('+ json.request_number +")")
		}, 
	});
};

$(document).ready(function (){
	setInterval(add_request_number,1000);
});