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


$(document).focus(function(){
	$.ajax({
		type:"GET",
		url:"/request_upload",
		data:{},

		success:function(json){
			var tbody_content = ''
			for(var i = 0;i<json.length;i++){
			    tbody_content += '<tr><th>'+ parseInt(i+1) +'</th><th>'+json[i].request_method+'</th><th>'+json[i].request_link+'</th><th>'+json[i].request_time+'</th></tr>'
			};
			$('tbody').html(tbody_content);
		},
	});
});