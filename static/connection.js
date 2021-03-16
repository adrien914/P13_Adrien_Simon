
function login(csrf_token) {
    "use strict";

    var input = $('.validate-input .input100');
    var check = true;
    let data = {}
    
    const username = document.getElementById('username').value
    const password = document.getElementById('password').value
    console.log(username, password)
    $.ajax({
        url: "/login/",
        type: 'POST',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrf_token},
        success: function () {
            location.reload()
        },
        error: function () {
            toastr.error('Erreur a la connexion!')
        }
    })

    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') === 'email' || $(input).attr('name') === 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() === ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    

}