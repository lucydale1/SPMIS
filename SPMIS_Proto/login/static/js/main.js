/**
 * Created by ojc on 30/04/2017.
 */
function create_post(ID){
    console.log("---Create POST----")
    console.log($('ID_' + ID + ' > .url-text').val())
    // console.log($form.find('.save-paper').val())
};

function add_fav(ID_in, url_in, title_in){
        $.ajax({
        url: "/results/",  // the endpoint
        type: "get",      // http method
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            ID: ID_in,
            url: url_in,
            title: title_in,
        },

        // handle a successful response
        success : function(json) {
            // console.log(json);
            console.log("Success");
            console.log(ID_in)
            console.log(url_in)
            console.log(title_in)
            $('#btn_' + ID_in + ' span')
                .removeClass('fa-star-o')
                .addClass('fa-star')
        },

        //handle a non-successful response
        error : function(xhr, errmsg, err){
            console.log(xhr.status + ": " + xhr.responseText);
        }
    })
};

// // Submit post on submit
// $(document).ready(function(){
//    $('.add-fav').click(function(event){
//         console.log("form submitted!")  // sanity check
//         event.preventDefault();
//
//         var ID = $(this).attr('id');
//
//         create_post(ID);
//         return false;
//     });
// });
