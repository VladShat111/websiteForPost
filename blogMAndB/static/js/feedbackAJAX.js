$(function(){
    $('#sendFeedback').click(function(event) {

        event.preventDefault();

        let feedbackUsername = $("#FeedUsername").val();
        let feedbackEmail = $("#FeedEmail").val();
        let feedbackMessage = $("#FeedMessage").val();
        $.ajax({
            type: 'POST',
            data: {'feedbackUsername': feedbackUsername ,
                    'feedbackEmail': feedbackEmail,
                    'feedbackMessage': feedbackMessage,
                    'csrfmiddlewaretoken': getCookie('csrftoken')
                   },

            success: function()
            {
                $( "#FeedbackState" ).append('<div class="alert alert-success" role="alert">Thanks for your feedback!</div>');
                $("#FeedUsername").val("");
            },
            error: function() {
                $( "#FeedbackState" )
                .append('<div class="alert alert-danger" role="alert">For some reason we can not save your feedback, please send email!</div>');
            },
            url: './feedback',
            cache: false
        });
        return false;
    });
}

);

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');