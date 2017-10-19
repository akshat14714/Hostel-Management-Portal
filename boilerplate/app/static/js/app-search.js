function search(name)
{
var x;
    $.ajax
    ({
    	method:"POST",
    	url:"http://127.0.0.1:8080/usersearch",
	async:false,
    	data:{name:name},
		success: function(input)
		{
		//	viewAllStudents();
			x=(input);
		},
		error: function(xhr,status,eThrown)
		{
			x=(status);
		},    
    });
return x;
}();
