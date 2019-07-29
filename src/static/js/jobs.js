$( document ).ready(function() {
    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    $('#job-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")
        var url = "/jobs/"+ slug +"/update/";
        $.ajax({ data: $(this).serialize(), 
            type: $(this).attr('method'), 
            url: $(this).attr('action'), 
            success: function(response) {
                 console.log(response);
                 if(response['success']) {
                    $("#results").html("<div class='alert alert-success'>\
                                Succesfully updated job details. View 'Preview' tab for changes.</div>");
                    $("#job_name").html(response.name);
                    $("#description").html(response.description);
                    $("#positions").html(response.positions);
                    
                 } 
                 if(response['error']) {
                     $("#results").html("<div class='alert alert-danger'>" +
                           response.error+"</div>");
                 } 
            },
            error: function (request, status, error) {
                 console.log(request.responseText);
            }
   });
    });
});
